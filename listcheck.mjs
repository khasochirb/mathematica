import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
const errs = [];
p.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
// seed a saved result the way the runner would, for a signed-out visitor
await p.goto('http://localhost:3000/math/integrated-1/exam', { waitUntil: 'networkidle' });
const before = await p.locator('text=/Start/').count();
const labels = await p.locator('text=/Practice Exam/').count();
const meta = await p.locator('text=/36 questions/').count();
console.log(JSON.stringify({ labels, startBadges: before, metaShown: meta, errs }, null, 1));
await b.close();
