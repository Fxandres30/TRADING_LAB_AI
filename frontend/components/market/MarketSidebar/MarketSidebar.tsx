import "./MarketSidebar.css";

import MarketInfo from "./MarketInfo/MarketInfo";
import Indicators from "./Indicators/Indicators";
import SmartMoney from "./SmartMoney/SmartMoney";

export default function MarketSidebar() {
    return (
        <aside className="market-sidebar">
            <MarketInfo />
            <Indicators />
            <SmartMoney />
        </aside>
    );
}