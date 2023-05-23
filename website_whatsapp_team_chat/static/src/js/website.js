odoo.define('website_whatsapp_team_chat', function (require) {
"use strict";
    $(document).ready(function(){
        $(".o_thread_window_header").click(function(){
            if($(".o_whatsapp_thread_window").css("height") == "400px"){
                $(".o_whatsapp_thread_window").css("height", "47px");
            }
            else{
                $(".o_whatsapp_thread_window").css("height", "400px");
            }
        });
    });

});
