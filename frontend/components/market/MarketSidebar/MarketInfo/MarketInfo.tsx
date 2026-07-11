import "./MarketInfo.css";

export default function MarketInfo() {
    return (
        <section className="market-card">

            <div className="card-header">
                <h3>📊 Información del Mercado</h3>
            </div>

            <div className="card-content">

                <div className="info-row">
                    <span>Activo</span>
                    <strong>EURUSD</strong>
                </div>

                <div className="info-row">
                    <span>Precio</span>
                    <strong>1.08452</strong>
                </div>

                <div className="info-row">
                    <span>Spread</span>
                    <strong>0.4 pips</strong>
                </div>

                <div className="info-row">
                    <span>Sesión</span>
                    <strong>Londres</strong>
                </div>

                <div className="info-row">
                    <span>Volatilidad</span>
                    <strong className="green">Alta</strong>
                </div>

                <div className="info-row">
                    <span>Actualización</span>
                    <strong>23:45:10</strong>
                </div>

            </div>

        </section>
    );
}