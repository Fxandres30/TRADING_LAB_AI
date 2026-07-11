import {
    createChart,
    IChartApi,
    ISeriesApi,
    CandlestickData,
} from "lightweight-charts";

import { chartOptions } from "./chartConfig";

import { CandleService } from "../services/CandleService";
import { candles } from "../data/candles";

export class ChartManager {

    private chart: IChartApi;

    private candleSeries: ISeriesApi<"Candlestick">;

    constructor(container: HTMLDivElement) {

        this.chart = createChart(container, chartOptions);

        this.candleSeries = this.chart.addCandlestickSeries({

            upColor: "#22c55e",
            downColor: "#ef4444",

            borderUpColor: "#22c55e",
            borderDownColor: "#ef4444",

            wickUpColor: "#22c55e",
            wickDownColor: "#ef4444",

            borderVisible: false,

        });

    }

    // =====================================
    // CARGAR HISTORIAL
    // =====================================

    async loadHistory(

        symbol: string = "EURUSD",

        timeframe: string = "M15"

    ) {

        try {

            const history = await CandleService.getHistory(

                symbol,

                timeframe

            );

            this.candleSeries.setData(

                history as CandlestickData[]

            );

            console.log(

                "✅ Historial cargado:",

                history.length,

                "velas"

            );

        }

        catch (error) {

            console.warn(

                "⚠ No se pudo cargar el historial, usando datos locales."

            );

            console.error(error);

            this.candleSeries.setData(candles);

        }

        this.chart.timeScale().fitContent();

    }

    // =====================================
    // ACTUALIZAR UNA VELA
    // =====================================

    updateCandle(candle: CandlestickData) {

        this.candleSeries.update(candle);

    }

    // =====================================
    // LIMPIAR
    // =====================================

    clear() {

        this.candleSeries.setData([]);

    }

    // =====================================
    // AUTO RESIZE
    // =====================================

    resize(width: number, height: number) {

        this.chart.applyOptions({

            width,

            height,

        });

    }

    // =====================================
    // ACCESO AL CHART
    // =====================================

    getChart() {

        return this.chart;

    }

    getSeries() {

        return this.candleSeries;

    }

    // =====================================
    // DESTRUIR
    // =====================================

    destroy() {

        this.chart.remove();

    }

}