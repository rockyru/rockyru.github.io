// Emails from the Ru Bot contact flow, in the layout of the 24/7 PULSE documents:
// the mark with two columns of context, a black band with three facts, numbered
// sections (number and heading left, content right), facts as grey rows, a faint
// dot grid across the foot. Inline styles and tables only; mail apps ignore stylesheets.

const SITE = "rmbergonia.com";
const LOGO = `https://${SITE}/images/rmb-mark.png`;
const DOTS = `https://${SITE}/images/email-dots.png`;
const SANS = "Inter,-apple-system,BlinkMacSystemFont,'Helvetica Neue',Helvetica,Arial,sans-serif";
const MONO = "SFMono-Regular,Menlo,Consolas,'Courier New',monospace";
const INK = "#000000", GREY = "#6B6B6B", LABEL = "#A3A3A3", RULE = "#E3E3E0", ROW = "#F3F3F1", PAPER = "#EDEDEA";

const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const manila = d => manilaLong(d);
const dateOnly = d => d.toLocaleDateString("en-GB", { timeZone: "Asia/Manila", day: "numeric", month: "long", year: "numeric" }); // 22 October 2026
const manilaLong = d => `${dateOnly(d)}, ${d.toLocaleTimeString("en-PH", { timeZone: "Asia/Manila", hour: "numeric", minute: "2-digit" })} PHT`;

export const paragraphs = text => String(text).trim().split(/\n\s*\n/)
  .map(p => `<p style="margin:0 0 10px;font-size:14px;line-height:1.75;">${esc(p).replace(/\n/g, "<br>")}</p>`).join("");

// Facts like the PDF's cost table: grey rows, value on the right.
export const facts = rows => `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:4px 0 12px;">${rows.map(([k, v, href]) => `
  <tr>
    <td valign="top" style="padding:9px 12px;background:${ROW};border-bottom:3px solid #ffffff;font-size:13px;line-height:1.5;">${esc(k)}</td>
    <td valign="top" align="right" style="padding:9px 12px;background:${ROW};border-bottom:3px solid #ffffff;font-size:13px;line-height:1.5;word-break:break-word;">${href ? `<a href="${esc(href)}" style="color:${INK};">${esc(v)}</a>` : esc(v)}</td>
  </tr>`).join("")}</table>`;

export const button = (href, label) => `<table role="presentation" cellpadding="0" cellspacing="0" style="margin:4px 0 12px;"><tr>
  <td style="background:${INK};"><a href="${esc(href)}" style="display:inline-block;padding:12px 20px;color:#ffffff;font-size:14px;font-weight:500;text-decoration:none;">${esc(label)} &rarr;</a></td>
</tr></table>`;

/**
 * The document. col1/col2: two lines each for the header columns. band: three [label, value].
 * sections: [heading, html]. hint: small grey line at the end. preview: inbox preview text.
 */
export function document({ title, preview, col1, col2, band, sections, hint }) {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light only">
<title>${esc(title)}</title>
<style>
  @media (max-width: 600px) {
    .px { padding-left: 20px !important; padding-right: 20px !important; }
    .stack { display: block !important; width: auto !important; }
    .band-cell { padding: 14px 0 0 !important; }
    .band-last { padding-bottom: 22px !important; }
    .side { padding: 18px 0 8px !important; border-top: 1px solid ${RULE} !important; }
    .main { padding: 0 0 22px !important; border-top: 0 !important; }
    .hdr-col { display: block !important; width: auto !important; padding-top: 8px !important; }
  }
</style>
</head>
<body style="margin:0;padding:0;background:${PAPER};font-family:${SANS};color:${INK};-webkit-text-size-adjust:100%;">
${preview ? `<div style="display:none;max-height:0;overflow:hidden;opacity:0;">${esc(preview)}&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;</div>` : ""}
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:${PAPER};">
<tr><td align="center" style="padding:28px 0;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:640px;background:#ffffff;">

    <!-- The mark, who sends it, who it is for -->
    <tr><td class="px" style="padding:34px 44px 30px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
        <td valign="top" style="width:150px;"><a href="https://${SITE}/" style="text-decoration:none;"><img src="${LOGO}" width="40" height="40" alt="Ruther Bergonia" style="display:block;width:40px;height:40px;border:0;"></a></td>
        <td valign="top" class="hdr-col" style="width:190px;font-size:12px;line-height:1.75;color:${INK};">${esc(col1[0])}<br>${esc(col1[1])}</td>
        <td valign="top" class="hdr-col" style="font-size:12px;line-height:1.75;color:${INK};">${esc(col2[0])}<br>${esc(col2[1])}</td>
      </tr></table>
    </td></tr>

    <!-- The band: three facts on black -->
    <tr><td class="px" style="padding:0 44px;background:${INK};color:#ffffff;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
        ${band.map(([label, value], i) => `
        <td valign="top" class="stack band-cell${i === band.length - 1 ? " band-last" : ""}" style="${i === 0 ? "width:150px;" : i === 1 ? "width:190px;" : ""}padding:30px 14px 32px 0;">
          <p style="margin:0 0 12px;font-size:11px;line-height:1;color:${LABEL};">${esc(label)}</p>
          <p style="margin:0;font-size:20px;line-height:1.3;font-weight:500;letter-spacing:-0.2px;word-break:break-word;">${esc(value)}</p>
        </td>`).join("")}
      </tr></table>
    </td></tr>

    <!-- Numbered sections -->
    <tr><td class="px" style="padding:30px 44px 0;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
        ${sections.map(([heading, html], i) => `
        <tr>
          <td valign="top" class="stack side" style="width:138px;padding:18px 12px 26px 0;border-top:1px solid ${RULE};">
            <p style="margin:0 0 9px;font-family:${MONO};font-size:10px;line-height:1;letter-spacing:0.5px;">${String(i + 1).padStart(2, "0")}</p>
            <p style="margin:0;font-size:19px;line-height:1.3;font-weight:500;letter-spacing:-0.2px;">${esc(heading)}</p>
          </td>
          <td valign="top" class="stack main" style="padding:39px 0 26px;border-top:1px solid ${RULE};font-size:14px;line-height:1.75;">${html}</td>
        </tr>`).join("")}
      </table>
    </td></tr>

    ${hint ? `<tr><td class="px" style="padding:6px 44px 0;"><p style="margin:0;font-size:12px;line-height:1.6;color:${GREY};">${hint}</p></td></tr>` : ""}

    <!-- The foot: the site's dot grid, faint, edge to edge -->
    <tr><td style="padding:26px 0 0;"><img src="${DOTS}" width="640" alt="" style="display:block;width:100%;max-width:640px;height:auto;border:0;"></td></tr>
  </table>
</td></tr>
</table>
</body>
</html>`;
}

/** The message Ruther receives. */
export function contactEmail({ name, email, message, ip, country, when = new Date() }) {
  const firstName = name.trim().split(" ")[0] || name;
  const firstLine = message.trim().split("\n")[0].slice(0, 70);
  const subject = `${name}: ${firstLine}${message.trim().length > firstLine.length ? "…" : ""}`;
  const replyHref = `mailto:${email}?subject=${encodeURIComponent("Re: your message on " + SITE)}`;
  const html = document({
    title: subject,
    preview: `${name} wrote through Ru Bot: ${firstLine}`,
    col1: ["Ruther Bergonia", SITE],
    col2: [name, "Website message"],
    band: [["Date", dateOnly(when)], ["From", name], ["Subject", "Message via Ru Bot"]],
    sections: [
      ["Message", paragraphs(message)],
      ["Sender", facts([["Name", name], ["Email", email, "mailto:" + email], ["Received", manila(when)], ["Origin", `${ip || "unknown"}${country ? " · " + country : ""}`]])],
      ["Reply", `<p style="margin:0 0 12px;font-size:14px;line-height:1.75;">Reply to this email, or use the button. Either way it goes to ${esc(name)}; the reply-to address is set.</p>` + button(replyHref, `Reply to ${firstName}`)],
    ],
    hint: `Sent through the Ru Bot contact flow on ${esc(SITE)} after the honeypot, timing and rate checks. The sender's details are as typed and were not verified.`,
  });
  const text = `${message.trim()}

—
From: ${name} <${email}>
Received: ${manila(when)}
Origin: ${ip || "unknown"}${country ? " · " + country : ""}
Via: Ru Bot on ${SITE}`;
  return { subject, html, text };
}

/**
 * The "we got your message" note the visitor receives. Deliberately does not echo
 * the message body, so the contact flow can't relay text to someone else's inbox.
 */
export function confirmationEmail({ name, when = new Date() }) {
  const firstName = name.trim().split(" ")[0] || name;
  const subject = `Got your message, ${firstName}`;
  const html = document({
    title: subject,
    preview: "I read every message myself and reply within one business day.",
    col1: ["Ruther Bergonia", SITE],
    col2: [name, "Message received"],
    band: [["Date", dateOnly(when)], ["For", name], ["Subject", "Your message to Ruther"]],
    sections: [
      ["Received", `<p style="margin:0 0 10px;font-size:14px;line-height:1.75;">Thanks, ${esc(firstName)}. Your message reached me through Ru Bot on ${esc(SITE)} at ${esc(manila(when))}. I read every message myself, so you'll hear back from me directly, within one business day.</p>`],
      ["What helps", `<p style="margin:0 0 10px;font-size:14px;line-height:1.75;">If any of these come to mind in the meantime, reply to this email and they land in the same thread:</p>` + facts([["Timeline", "Rough dates, if you have them"], ["Budget", "A range is enough"], ["Systems", "Anything this needs to work with"]])],
      ["While you wait", `<p style="margin:0 0 12px;font-size:14px;line-height:1.75;">The case studies show how I've built similar systems: what was actually hard, and what shipped.</p>` + button(`https://${SITE}/work/`, "See the case studies")],
    ],
    hint: `Didn't send a message on ${esc(SITE)}? Someone may have typed your address by mistake. You can ignore this email; nothing else will be sent.`,
  });
  const text = `Thanks, ${firstName}. Your message reached me through Ru Bot on ${SITE} at ${manila(when)}. I read every message myself, so you'll hear back from me directly, within one business day.

If any of these come to mind in the meantime, reply to this email: a rough timeline, a budget range, any systems this needs to work with.

Case studies: https://${SITE}/work/

Ruther Bergonia · Software systems architect & senior full-stack engineer · Metro Manila
Didn't send a message on ${SITE}? You can ignore this email; nothing else will be sent.`;
  return { subject, html, text };
}
