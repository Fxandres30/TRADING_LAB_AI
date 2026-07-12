import AccountDetectedCard from "./AccountDetectedCard";
import { Account } from "./types";

type Props = {
    accounts: Account[];
    onConnect: (account: Account) => void;
};

export default function AccountDetectedList({
    accounts,
    onConnect,
}: Props) {

    if (accounts.length === 0) {
        return (
            <div className="empty">
                No se encontraron cuentas.
            </div>
        );
    }

    return (
        <>
            {accounts.map((account) => (
                <AccountDetectedCard
                    key={`${account.broker}-${account.login}`}
                    account={account}
                    onConnect={onConnect}
                />
            ))}
        </>
    );
}