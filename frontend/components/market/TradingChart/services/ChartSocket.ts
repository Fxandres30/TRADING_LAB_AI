export class ChartSocket{

    socket:WebSocket|null=null;

    connect(){

        this.socket=new WebSocket(

            "ws://127.0.0.1:8000/ws/chart"

        );

    }

    onMessage(callback:(data:any)=>void){

        if(!this.socket) return;

        this.socket.onmessage=(event)=>{

            callback(

                JSON.parse(event.data)

            );

        };

    }

}