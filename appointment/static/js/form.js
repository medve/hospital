function get_free_time(){
  console.log("a");
  if( $("#id_doctor").val() && $("#id_appointment_date").val()){
    console.log("b");
    $.getJSON("/get_free_time/",
              {"doctor": $("#id_doctor").val(),
               "appointment_date": $("#id_appointment_date").val()},
        function(data){
          $("#id_appointment_hour").empty();
          for( var i=0; i < data['times'].length; i++ ){
            $("#id_appointment_hour").append("<option value="
                                             +data['times'][i]+">"
                                             +data['times'][i]+":00</option>");
          }
        $("#id_appointment_hour").prop("disabled",false);
      });
  }
}

$(document).ready(function(){
  $("#id_appointment_hour").prop( "disabled", true );
});

$("#id_doctor").change(get_free_time);

$("#id_appointment_date").change(get_free_time);
