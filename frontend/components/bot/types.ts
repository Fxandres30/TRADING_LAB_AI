export interface StrategyStats{

    operaciones:number;

    ganadas:number;

    perdidas:number;

    win_rate:number;

    rentabilidad:number;

    profit_factor:number;

    drawdown:number;

    ganancia_total:number;

    perdida_total:number;

    mayor_ganancia:number;

    mayor_perdida:number;

    racha_ganadora:number;

    racha_perdedora:number;

    tiempo_promedio:string;

    tiempo_minimo:string;

    tiempo_maximo:string;

    score:number;

}

export interface Strategy{

    id:string;

    codigo:string;

    nombre:string;

    descripcion:string;

    activa:boolean;

    categoria:string;

    version:string;

    stats:StrategyStats;

}
