function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken'); 
    $('#codigo_repuesto').on('keydown', function(event) {

        if (event.keyCode === 13) { 
            event.preventDefault(); 
            var codigo_repuesto = $(this).val();

            $.ajax({
                url: autocompletar_repuestoURL,
                method: 'POST',
                data: { 
                    codigo_repuesto: codigo_repuesto,
                    csrfmiddlewaretoken: csrftoken 
                },
                success: function(response) {
                    $('#nombre_repuesto').val(response.data.nombre_repuesto);
                    $('#descripcion_repuesto').val(response.data.descripcion_repuesto);
                        
                    var base64File = response.data.foto_repuesto; 

                    if (base64File) {
                        try {
                            var decodedFile = atob(base64File);
                            var decodedFile = decodedFile;
                            var staticPath = "/static/imgRepuestos/";
                            var srcPath = staticPath + decodedFile
                            var cleanSrcPath = srcPath.replace(/'/g, '');
                            $('#foto_repuesto').attr('src', cleanSrcPath);

                        } catch (error) {
                            $('#foto_repuesto').attr('src', '/static/imgRepuestos/default_image.png');
                        }
                    } else {
                        $('#foto_repuesto').attr('src', '/static/imgRepuestos/default_image.png');
                    }
                },
                error: function() {
                    $('#foto_repuesto').attr('src', '/static/imgRepuestos/default_image.png');
                }
            });
        }
    });
});

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken'); 
    $('#codigo_proveedor').on('keydown', function(event) {
            
        if (event.keyCode === 13) { 
            event.preventDefault(); 
            var codigo_proveedor = $(this).val();

            $.ajax({
                url: autocompletar_proveedorURL,  
                method: 'POST',
                data: { codigo_proveedor: codigo_proveedor,
                    csrfmiddlewaretoken: csrftoken 
                },
                success: function(response) {
                    console.log(response);
                    console.log(response.data); 
                    $('#razon_social_proveedor').val(response.data);
                }                
            });
        }
    });
});

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken'); 

    $('form').on('submit', function(event) {
        event.preventDefault(); 

        var codigo_repuesto = $('#codigo_repuesto').val();
        var cantidad_entrada_repuesto = $('#cantidad_entrada_repuesto').val();
        var codigo_proveedor = $('#codigo_proveedor').val();
        var fecha_entrada_repuesto = $('#fecha_entrada_repuesto').val();

        $.ajax({
            url: registro_entradaURL, 
            method: 'POST',
            data: {
                codigo_repuesto: codigo_repuesto,
                cantidad_entrada_repuesto: cantidad_entrada_repuesto,
                codigo_proveedor: codigo_proveedor,
                fecha_entrada_repuesto: fecha_entrada_repuesto, 
                csrfmiddlewaretoken: csrftoken 
            },
            success: function(response) {
                console.log('Entrada registrada exitosamente');
                window.location.reload(); 
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
