import "./Indicators.css";

export default function Indicators() {

    return (

        <section className="market-card">

            <div className="card-header">
                <h3>📈 Indicadores</h3>
            </div>

            <div className="card-content">

                <div className="info-row">
                    <span>EMA 20</span>
                    <strong className="green">Bullish</strong>
                </div>

                <div className="info-row">
                    <span>EMA 50</span>
                    <strong className="green">Bullish</strong>
                </div>

                <div className="info-row">
                    <span>RSI</span>
                    <strong>64.20</strong>
                </div>

                <div className="info-row">
                    <span>MACD</span>
                    <strong className="green">Compra</strong>
                </div>

                <div className="info-row">
                    <span>ATR</span>
                    <strong>Alto</strong>
                </div>

                <div className="info-row">
                    <span>ADX</span>
                    <strong>31</strong>
                </div>

            </div>

        </section>

    );

}