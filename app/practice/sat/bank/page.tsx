import BankUnitList from "@/components/bank/BankUnitList";
import { SAT_BANK_CHROME } from "@/components/bank/bank-chrome";
import { getSatBankTopic } from "@/lib/bank-data";

export const metadata = { title: "SAT Math · Topic Practice" };

// The SAT hub's topic-focused practice branch (resource blueprint: every hub
// offers Tests · Courses · Topic practice in ITS OWN taxonomy). One bank
// topic, organized by the four Digital SAT domains, served by the same bank
// machinery as /math/problem-bank — only the chrome differs.
export default function SatBankPage() {
  return <BankUnitList topic={getSatBankTopic()} chrome={SAT_BANK_CHROME} />;
}
