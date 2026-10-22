// The email Ruther receives when someone writes through Ru Bot.
// Layout borrowed from the 24/7 PULSE documents: a mark row, a black band with three facts,
// numbered sections (heading left, content right), a reply button, a quiet footer.
// Inline styles and tables only, because mail apps ignore stylesheets.

const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const SANS = "Inter,-apple-system,BlinkMacSystemFont,'Helvetica Neue',Helvetica,Arial,sans-serif";
const MONO = "SFMono-Regular,Menlo,Consolas,monospace";
const LOGO = "https://rmbergonia.com/images/rmb-mark.png";
const logoImg = (size, alt = "Ruther Bergonia") => `<img src="${LOGO}" width="${size}" height="${size}" alt="${esc(alt)}" style="display:block;width:${size}px;height:${size}px;border:0;">`;

function paragraphs(text) {
  return String(text).trim().split(/\n\s*\n/).map(p => `<p style="margin:0 0 12px;">${esc(p).replace(/\n/g, "<br>")}</p>`).join("");
}
function facts(rows) {
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 4px;">${rows.map(([k, v, href]) => `
    <tr>
      <td valign="top" style="width:96px;padding:8px 10px;background:#F3F3F1;border-bottom:3px solid #ffffff;font-size:12px;line-height:1.5;color:#6B6B6B;">${esc(k)}</td>
      <td valign="top" style="padding:8px 10px;background:#F3F3F1;border-bottom:3px solid #ffffff;font-size:14px;line-height:1.5;word-break:break-word;">${href ? `<a href="${esc(href)}" style="color:#000000;">${esc(v)}</a>` : esc(v)}</td>
    </tr>`).join("")}</table>`;
}

export function contactEmail({ name, email, message, ip, country, when = new Date(), site = "rmbergonia.com" }) {
  const received = when.toLocaleString("en-PH", { timeZone: "Asia/Manila", dateStyle: "medium", timeStyle: "short" }) + " PHT";
  const firstLine = message.trim().split("\n")[0].slice(0, 70);
  const subject = `New message from ${name} via Ru Bot`;
  const preview = `${name}: ${firstLine}`;
  const replyHref = `mailto:${email}?subject=${encodeURIComponent("Re: your message on " + site)}`;
  const sections = [
    ["Message", paragraphs(message)],
    ["Sender", facts([["Name", name], ["Email", email, "mailto:" + email], ["Received", received], ["Origin", `${ip || "unknown"}${country ? " · " + country : ""}`]])],
  ];

  const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light only">
<title>${esc(subject)}</title>
<style>
  @media (max-width: 600px) {
    .px { padding-left: 20px !important; padding-right: 20px !important; }
    .stack { display: block !important; width: auto !important; }
    .band-cell { padding: 14px 0 0 !important; }
    .band-last { padding-bottom: 20px !important; }
    .sec-side { padding: 18px 0 8px !important; border-top: 1px solid #E3E3E0 !important; }
    .sec-main { padding: 0 0 22px !important; border-top: 0 !important; }
  }
</style>
</head>
<body style="margin:0;padding:0;background:#EDEDEA;font-family:${SANS};color:#000000;-webkit-text-size-adjust:100%;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">${esc(preview)}&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EDEDEA;">
<tr><td align="center" style="padding:28px 0;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:640px;background:#ffffff;border:1px solid #000000;">

    <tr><td class="px" style="padding:30px 44px 26px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
        <td valign="top" style="width:150px;">${logoImg(28)}</td>
        <td valign="top" style="font-size:11px;line-height:1.6;">Ruther Bergonia<br>${esc(site)}</td>
        <td valign="top" style="font-size:11px;line-height:1.6;">Ru Bot<br>Website message</td>
      </tr></table>
    </td></tr>

    <tr><td class="px" style="padding:0 44px;background:#000000;color:#ffffff;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
        <td valign="top" class="stack band-cell" style="width:150px;padding:26px 12px 28px 0;">
          <p style="margin:0 0 10px;font-size:11px;line-height:1;color:#A3A3A3;">From</p>
          <p style="margin:0;font-size:18px;line-height:1.3;font-weight:500;">${esc(name)}</p>
        </td>
        <td valign="top" class="stack band-cell" style="width:200px;padding:26px 12px 28px 0;">
          <p style="margin:0 0 10px;font-size:11px;line-height:1;color:#A3A3A3;">Reply to</p>
          <p style="margin:0;font-size:18px;line-height:1.3;font-weight:500;word-break:break-all;"><a href="mailto:${esc(email)}" style="color:#ffffff;text-decoration:none;">${esc(email)}</a></p>
        </td>
        <td valign="top" class="stack band-cell band-last" style="padding:26px 0 28px;">
          <p style="margin:0 0 10px;font-size:11px;line-height:1;color:#A3A3A3;">Received</p>
          <p style="margin:0;font-size:18px;line-height:1.3;font-weight:500;">${esc(received)}</p>
        </td>
      </tr></table>
    </td></tr>

    <tr><td class="px" style="padding:30px 44px 6px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
        ${sections.map(([heading, body], i) => `
        <tr>
          <td valign="top" class="stack sec-side" style="width:138px;padding:16px 12px 24px 0;border-top:1px solid #E3E3E0;">
            <p style="margin:0 0 8px;font-family:${MONO};font-size:10px;line-height:1;letter-spacing:0.5px;">${String(i + 1).padStart(2, "0")}</p>
            <p style="margin:0;font-size:18px;line-height:1.2;font-weight:500;">${esc(heading)}</p>
          </td>
          <td valign="top" class="stack sec-main" style="padding:16px 0 24px;border-top:1px solid #E3E3E0;font-size:14px;line-height:1.7;">${body}</td>
        </tr>`).join("")}
      </table>
    </td></tr>

    <tr><td class="px" style="padding:4px 44px 34px;">
      <table role="presentation" cellpadding="0" cellspacing="0"><tr>
        <td style="background:#000000;"><a href="${esc(replyHref)}" style="display:inline-block;padding:12px 20px;color:#ffffff;font-size:14px;font-weight:500;text-decoration:none;">Reply to ${esc(name.split(" ")[0])} &rarr;</a></td>
      </tr></table>
      <p style="margin:14px 0 0;font-size:12px;line-height:1.6;color:#6B6B6B;">Replying to this email also goes straight to ${esc(name)}; the reply-to address is set. Sent through the Ru Bot contact flow on ${esc(site)}, after the honeypot, timing and rate checks.</p>
    </td></tr>
  </table>
  <p style="max-width:640px;margin:14px auto 0;padding:0 20px;font-size:11px;line-height:1.6;color:#6B6B6B;box-sizing:border-box;">You get this because someone used the contact flow on your site. The sender's details are as they typed them and were not verified.</p>
</td></tr>
</table>
</body>
</html>`;

  const text = `${message.trim()}

—
From: ${name} <${email}>
Received: ${received}
Origin: ${ip || "unknown"}${country ? " · " + country : ""}
Via: Ru Bot on ${site}`;

  return { subject, html, text };
}

// The "we got your message" note the visitor receives. Deliberately does not echo the
// message body, so the contact flow can't be used to relay text to someone else's inbox.
export function confirmationEmail({ name, when = new Date(), site = "rmbergonia.com" }) {
  const first = esc(name.trim().split(" ")[0] || name);
  const received = when.toLocaleString("en-PH", { timeZone: "Asia/Manila", dateStyle: "medium", timeStyle: "short" }) + " PHT";
  const subject = `Got your message, ${first}`;
  const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light only">
<title>${esc(subject)}</title>
</head>
<body style="margin:0;padding:0;background:#EDEDEA;font-family:${SANS};color:#000000;-webkit-text-size-adjust:100%;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">Ruther reads every message himself and replies within one business day.&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EDEDEA;">
<tr><td align="center" style="padding:28px 12px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:580px;border:1px solid #000000;">

    <tr><td style="background:#000000;padding:22px 28px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
        <td valign="middle">
          <a href="https://${esc(site)}/" style="text-decoration:none;color:#ffffff;">
            <table role="presentation" cellpadding="0" cellspacing="0"><tr>
              <td valign="middle" style="padding-right:10px;"><img src="${LOGO}" width="26" height="26" alt="" style="display:block;width:26px;height:26px;border:0;filter:invert(1);"></td>
              <td valign="middle" style="font-size:15px;font-weight:700;color:#ffffff;letter-spacing:-0.2px;">Ruther Bergonia</td>
            </tr></table>
          </a>
        </td>
        <td valign="middle" align="right" style="font-size:11px;line-height:1.4;letter-spacing:.14em;text-transform:uppercase;color:#A3A3A3;padding-left:12px;">Systems architect · Manila</td>
      </tr></table>
    </td></tr>
    <tr><td style="background:#22c55e;height:5px;line-height:5px;font-size:0;">&nbsp;</td></tr>

    <tr><td style="background:#ffffff;padding:32px 28px 30px;">
      <p style="margin:0 0 10px;font-size:11px;line-height:1.4;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:#6B6B6B;">Message received</p>
      <h1 style="margin:0 0 20px;font-size:28px;line-height:1.1;font-weight:800;letter-spacing:-0.5px;color:#000000;">Thanks, ${first}. I'll reply within one business day.</h1>
      <p style="margin:0 0 16px;font-size:16px;line-height:1.65;color:#2A2A2A;">Your message reached me through Ru Bot on ${esc(site)} at ${esc(received)}. I read every message myself, so you'll hear back from me directly, not from a bot.</p>
      <p style="margin:0 0 16px;font-size:16px;line-height:1.65;color:#2A2A2A;">If anything useful comes to mind in the meantime, like a rough timeline, a budget range, or the systems this needs to work with, just reply to this email and it lands in the same thread.</p>
      <table role="presentation" cellpadding="0" cellspacing="0" style="margin:8px 0 0;"><tr>
        <td style="border-left:3px solid #000000;padding:2px 0 2px 12px;">
          <p style="margin:0;font-size:15px;font-weight:700;color:#000000;">Ruther Bergonia</p>
          <p style="margin:2px 0 0;font-size:13px;color:#6B6B6B;">Software systems architect &amp; senior full-stack engineer</p>
        </td>
      </tr></table>
      <table role="presentation" cellpadding="0" cellspacing="0" style="margin:26px 0 0;"><tr>
        <td style="background:#000000;"><a href="https://${esc(site)}/work/" style="display:inline-block;padding:13px 22px;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#ffffff;text-decoration:none;">See the case studies &rarr;</a></td>
      </tr></table>
    </td></tr>

    <tr><td style="background:#ffffff;padding:0 28px 26px;">
      <p style="margin:0;padding:14px 16px;background:#F3F3F1;font-size:13px;line-height:1.55;color:#6B6B6B;">Didn't send a message on ${esc(site)}? Someone may have typed your address by mistake. You can ignore this email; nothing else will be sent.</p>
    </td></tr>

    <tr><td style="background:#000000;padding:22px 28px;">
      <p style="margin:0 0 6px;font-size:15px;line-height:1.2;font-weight:700;color:#ffffff;">Ruther Bergonia</p>
      <p style="margin:0;font-size:13px;line-height:1.7;color:#A3A3A3;">Metro Manila, Philippines &nbsp;·&nbsp; <a href="https://${esc(site)}/" style="color:#ffffff;text-decoration:none;">${esc(site)}</a> &nbsp;·&nbsp; <a href="mailto:ruther.bergonia@gmail.com" style="color:#ffffff;text-decoration:none;">ruther.bergonia@gmail.com</a></p>
    </td></tr>
  </table>
</td></tr>
</table>
</body>
</html>`;
  const text = `Thanks, ${name.trim().split(" ")[0]}. I'll reply within one business day.

Your message reached me through Ru Bot on ${site} at ${received}. I read every message myself, so you'll hear back from me directly.

If anything useful comes to mind in the meantime (a rough timeline, a budget range, the systems this needs to work with), just reply to this email.

Ruther Bergonia
Software systems architect & senior full-stack engineer
Metro Manila, Philippines · https://${site}/ · ruther.bergonia@gmail.com

Didn't send a message on ${site}? You can ignore this email; nothing else will be sent.`;
  return { subject, html, text };
}
