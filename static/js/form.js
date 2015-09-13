function get_free_time(){
  if( $("#id_doctor").value !== undefined  && 
      $("#id_appointment_date").value !== undefined){
    $.getJSON("/get_free_time/",{"doctor": $("#id_doctor").value,
                                 "doctor": $("#id_appointment_date").value
                               }, function(data){
          for( var i=0; i < data['times'].length; i++ ){
            $("#id_appointment_hour").append("<option value="
                                             +data['times'][i]+">"
                                             +data['times'][i]+":00</option>");
          }
      $("#id_appointment_hour").removeProp("disabled");
      });
  }
}

$(document).ready(function(){
  $("#id_appointment_hour").prop( "disabled", true );
});

$("#id_doctor").change(get_free_time);

$("#id_appointment_date").change(get_free_time);
