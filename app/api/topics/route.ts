export const dynamic = "force-dynamic";

import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";

interface TopicRow {
  id: string;
  parent_id: string | null;
  name: string;
  slug: string;
  display_order: number;
}

interface TopicTree {
  id: string;
  name: string;
  slug: string;
  children?: TopicTree[];
}

export async function GET() {
  const admin = createAdminClient();

  const { data: rows, error } = await admin
    .from("topics")
    .select("id, parent_id, name, slug, display_order")
    .order("display_order", { ascending: true });

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  const topics = rows as TopicRow[];

  const topLevel: TopicTree[] = [];
  const childrenMap = new Map<string, TopicTree[]>();

  for (const t of topics) {
    if (t.parent_id) {
      const arr = childrenMap.get(t.parent_id) ?? [];
      arr.push({ id: t.id, name: t.name, slug: t.slug });
      childrenMap.set(t.parent_id, arr);
    }
  }

  for (const t of topics) {
    if (!t.parent_id) {
      const node: TopicTree = { id: t.id, name: t.name, slug: t.slug };
      const kids = childrenMap.get(t.id);
      if (kids && kids.length > 0) node.children = kids;
      topLevel.push(node);
    }
  }

  return NextResponse.json({ data: topLevel });
}
