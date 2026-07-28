#!/usr/bin/env node
/**
 * PostToolUse hook (Write|Edit) pro Fázi 2 tohoto projektu.
 *
 * Dva spouštěče, oba na zápis do content/<destinace>/text/:
 *  A) uložení/úprava kapitoly (content/<destinace>/text/<soubor>.md, mimo
 *     _fact-check/ a _shot-list/) -> pokud kapitola nemá aktuální fact-check,
 *     dá Claudovi v session najevo, ať spustí Fact-Checker subagenta.
 *  B) uložení fact-checku (content/<destinace>/text/_fact-check/<soubor>.md)
 *     -> pokud teď mají všechny kapitoly destinace "Stav: OK" a shot-list
 *     chybí/je zastaralý, dá Claudovi v session najevo, ať spustí
 *     Shot-List-Creator subagenta pro každou kapitolu destinace.
 *
 * Stav automatizace: docs/automation-registry.md.
 */

const fs = require("fs");
const path = require("path");

function emitAdditionalContext(text) {
  process.stdout.write(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: "PostToolUse",
        additionalContext: text,
      },
    })
  );
  process.exit(0);
}

function readStdin() {
  try {
    return fs.readFileSync(0, "utf8");
  } catch {
    return "";
  }
}

function main() {
  const raw = readStdin();
  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    process.exit(0);
  }

  if (data.tool_name !== "Write" && data.tool_name !== "Edit") process.exit(0);

  const filePath = data.tool_input && data.tool_input.file_path;
  if (!filePath) process.exit(0);

  const normalized = filePath.replace(/\\/g, "/");

  const factCheckMatch = normalized.match(
    /\/content\/([^/]+)\/text\/_fact-check\/([^/]+\.md)$/
  );
  const shotListMatch = normalized.match(
    /\/content\/([^/]+)\/text\/_shot-list\/([^/]+\.md)$/
  );
  const chapterMatch = normalized.match(/\/content\/([^/]+)\/text\/([^/]+\.md)$/);

  // Kořen projektu se odvozuje z cesty upraveného souboru (část před /content/),
  // ne z CLAUDE_PROJECT_DIR — ten ukazuje na kořen session, který může být
  // o úroveň výš (řídící složka dp-prirucka), a cesty by pak nesedly.
  const match = factCheckMatch || shotListMatch || chapterMatch;
  if (!match) process.exit(0);
  const projectDir = normalized.slice(0, match.index);

  if (factCheckMatch) {
    handleFactCheckSave(factCheckMatch[1], projectDir);
  } else if (!shotListMatch && chapterMatch) {
    handleChapterSave(chapterMatch[1], chapterMatch[2], projectDir);
  } else {
    process.exit(0);
  }
}

function handleChapterSave(destination, fileName, projectDir) {
  const chapterPath = path.join(
    projectDir,
    "content",
    destination,
    "text",
    fileName
  );
  const factCheckPath = path.join(
    projectDir,
    "content",
    destination,
    "text",
    "_fact-check",
    fileName
  );

  let hasCurrentFactCheck = false;
  if (fs.existsSync(factCheckPath) && fs.existsSync(chapterPath)) {
    const fcMtime = fs.statSync(factCheckPath).mtimeMs;
    const chMtime = fs.statSync(chapterPath).mtimeMs;
    hasCurrentFactCheck = fcMtime >= chMtime;
  }

  if (hasCurrentFactCheck) process.exit(0);

  emitAdditionalContext(
    `[automation: fact-check-on-save] Kapitola "content/${destination}/text/${fileName}" byla právě uložena/upravena a nemá aktuální fact-check. ` +
      `Spusť teď, bez čekání na pokyn uživatele, nezávislého Fact-Checker subagenta (.claude/agents/fact-checker.md) pro tuto kapitolu — ` +
      `porovná ji proti content/${destination}/research/ a zapíše výstup do content/${destination}/text/_fact-check/${fileName}.`
  );
}

function handleFactCheckSave(destination, projectDir) {
  const textDir = path.join(projectDir, "content", destination, "text");
  const factCheckDir = path.join(textDir, "_fact-check");
  const shotListDir = path.join(textDir, "_shot-list");

  if (!fs.existsSync(textDir)) process.exit(0);

  const chapterFiles = fs
    .readdirSync(textDir)
    .filter((f) => f.endsWith(".md"))
    .filter((f) => fs.statSync(path.join(textDir, f)).isFile())
    .sort();

  if (chapterFiles.length === 0) process.exit(0);

  const okCount = chapterFiles.filter((f) => {
    const fcPath = path.join(factCheckDir, f);
    if (!fs.existsSync(fcPath)) return false;
    const content = fs.readFileSync(fcPath, "utf8");
    return /^Stav:\s*OK\s*$/m.test(content);
  }).length;

  if (okCount !== chapterFiles.length) process.exit(0);

  const needsShotList = chapterFiles.some((f) => {
    const slPath = path.join(shotListDir, f);
    if (!fs.existsSync(slPath)) return true;
    const chMtime = fs.statSync(path.join(textDir, f)).mtimeMs;
    const slMtime = fs.statSync(slPath).mtimeMs;
    return slMtime < chMtime;
  });

  if (!needsShotList) process.exit(0);

  const filesList = chapterFiles.map((f) => `content/${destination}/text/${f}`).join(", ");

  emitAdditionalContext(
    `[automation: fact-check-on-save] Všech ${chapterFiles.length} kapitol destinace "${destination}" má teď fact-check se stavem OK ` +
      `a shot-list v content/${destination}/text/_shot-list/ chybí nebo je starší než odpovídající kapitola. ` +
      `Spusť teď, bez čekání na pokyn uživatele, nezávislého Shot-List-Creator subagenta (.claude/agents/shot-list-creator.md) pro každou z těchto kapitol: ${filesList} — ` +
      `ulož výstupy do content/${destination}/text/_shot-list/<stejný-název>.md.`
  );
}

main();
