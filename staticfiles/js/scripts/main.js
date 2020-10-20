(function() {

$('#id_pdf').on('change', function(evt){
  // get the file name from - evt.target.files[0].name
  let name = evt.target.files[0].name
  name = name.length > 50 ? name.slice(150) : name
  $(this).next('.custom-file-label').html(name);
});

})()
