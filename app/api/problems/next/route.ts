import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({ error: "No problems available yet." }, { status: 404 });
}
