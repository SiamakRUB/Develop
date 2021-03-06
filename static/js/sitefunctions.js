﻿// https://www.tutorialspoint.com/jqueryui/jqueryui_slider.htm

$(document).ajaxStart(function(){
    $("#wait").css("display", "block");
  });
  
  $(document).ajaxComplete(function(){
    $("#wait").css("display", "none");
  });

$(function () {

    $(".form-group.row.slider-control").each(function () {
        var $slider = $(this).find('div.slider-drag');
        var $sliderlabel = $(this).find('input.slider-label');
        var $slidermaxval = $(this).find('input.slider-maxvalue');
        var $sliderminval = $(this).find('input.slider-minvalue');

        var minval = parseFloat($slider.data("min"));
        var maxval = parseFloat($slider.data("max"));

        $slider.slider({
            range: true,
            min: minval,
            max: maxval,
            values: [minval, maxval],
            slide: function (event, ui) {
                $sliderlabel.val(ui.values[0] + " - " + ui.values[1]);
                $sliderminval.val(ui.values[0]);
                $slidermaxval.val(ui.values[1]);
            }
        });
        $sliderlabel.val($slider.slider("values", 0) +
            " - " + $slider.slider("values", 1));
    });




    /****************************************
       *       Basic Table                   *
       ****************************************/

    ExportTable($('#Word_zero_config'), $('#Wordexport'));
    ExportTable($('#lemma_config'), $('#lemmaexport'));
    ExportTable($('#global_config'), $('#globalexport'));
    ExportTable($('#text_config'), $('#textexport'));
    
    // $('#GeneralView').DataTable({ searching: false });
    $('#Word_zero_config').DataTable();
    $('#lemma_config').DataTable({ searching: false });
    $('#global_config').DataTable({ searching: false });
    $('#text_config').DataTable({ searching: false });
    /****************************************
       *       Basic Table                   *
       * $('table').dataTable({searching: false, paging: false, info: false});
    For DataTables <1.10, use:
    
    $('table').dataTable({bFilter: false, bInfo: false});
    or using pure CSS:
    
    .dataTables_filter, .dataTables_info { display: none; }
       ****************************************/
    function ExportTable(table, divId) {
        var $myTable = table;
        // Run `tableExport()`
        $myTable.tableExport({ formats: ["xlsx", "csv"], });
        // Detach the `buttons` html
        var $buttons = $myTable.find('caption').children().detach();
        // Append the buttons to an element of your choosing
        $buttons.appendTo(divId);
    }

    // Checkbox Show Columns

    $('#btnshowgroup').click(function (e) {
        e.preventDefault();
        var showfields=[];
        var showfieldsLabel=[];
        $('.jqshowcolumn').each(function(){
            if($(this).is(":checked")){      
            fieldsname=$(this).data('field');
            fieldsnameshow=$(this).data('fieldlabel');
            showfields.push(fieldsname);
            showfieldsLabel.push(fieldsnameshow);
            }
        }); 
        $.ajax({
            url: '/ajax/ShowGroupSetting/',
            method : "post",
            data: {
              'showcols': showfields,'showfieldsLabel':showfieldsLabel,
              'csrfmiddlewaretoken': window.CSRF_TOKEN
            },
            success: function (data) {
              if (data.is_taken) {
                alert("A user with this username already exists.");
              }
            }
          });
    });
    /****************************************
  Multiselect
  /****************************************/


    var x= $('select.multi').selectpicker({
        onChange: function (element, checked) {
            console.log(selected);
        }
    });
    $('#searchform').submit(function (event) {
        $("#cover-spin").css("display", "block");
          
            var x= $(".btn.dropdown-toggle");
            x.each(function (){
                var selected=$(this).attr('title');
                var hdnfield=$(this).closest( ".form-group.row" ).find("input[type=hidden]").val(selected);
            })
          return true; //<---- move it here
        });
      

    /****************************************
  Chart
  /****************************************/


    var ctx = $("canvas.chart-litkey-line");
    var dataset = ctx.data("collection");
    var datasetlabel = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
    var datatitle = ctx.data("title");//Number of words
    var datacolor = ctx.data("color");//Number of words 
    var datatype = ctx.data("type");//Number of words 
    $("canvas.chart-litkey-age").each(function () {
        var ctx = $(this);
        var dataset = ctx.data("collection");
        var labels = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
        var datasetcategory ="";
        // if(labels != ''||labels != null){  
        // datasetcategory=ctx.data("label").replace('[', '').replace(']','')
        // var arrayxbase=datasetcategory.split(",");;
        //      }; 
        var datasetlabel = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
        var datatitle = ctx.data("title");//Number of words
        var datacolor = ctx.data("color");//Number of words 
        var datatype = ctx.data("type");//Number of words 
        var myChart = new Chart(ctx, {
            type: datatype,
            data: {
                labels: labels,
                datasets: [{
                    label: datatitle,
                    data: dataset,
                    backgroundColor: datacolor,
                }]
            }
        });
    });
    $("canvas.chart-litkey").each(function () {
        var ctx = $(this);
        var dataset = ctx.data("collection");
        var labels = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
        var datasetcategory ="";
        if(labels != ''&&labels != null){  
        datasetcategory=ctx.data("label").replace('[', '').replace(']','')
        var arrayxbase=datasetcategory.split(",");;
             }; 
        var datasetlabel = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
        var datatitle = ctx.data("title");//Number of words
        var datacolor = ctx.data("color");//Number of words 
        var datatype = ctx.data("type");//Number of words 
        var myChart = new Chart(ctx, {
            type: datatype,
            data: {
                labels: arrayxbase,
                datasets: [{
                    label: datatitle,
                    data: dataset,
                    backgroundColor: datacolor,
                }]
            }
        });
    });
    $("canvas.chart-litkey-bar").each(function () {
        var ctx = $(this);
        var dataset = ctx.data("collection");
        var labels = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
        var datatitle = ctx.data("title");//Number of words
        var datacolor = ctx.data("color");//Number of words 
        var datatype = ctx.data("type");//Number of words 
        var myChart = new Chart(ctx, {
            type: datatype,
            data: {
                labels: labels,
                datasets: [{
                    label: datatitle,
                    data: dataset,
                    backgroundColor: datacolor,
                }]
            }
        });
    });
    $("canvas.chart-litkey-line").each(function () {
        var ctx = $(this);
        

       
        var dataset = ctx.data("collection");
        var cats=ctx.data("category")
        var datasetcategory ="";
        if(cats != '' && cats != null){  
        datasetcategory=ctx.data("category").replace('[', '').replace(']','')
        var arrayxbase=datasetcategory.split(",");;
             };  
        var datasetlabel = ctx.data("label");//["7 ", "8-9 ", "10-11", "11-13"]
        var datatitle = ctx.data("title");//Number of words
        var datacolor = ctx.data("color");//Number of words 
        var datatype = ctx.data("type");//Number of words 
        var datasetML = ctx.data("multi");//Number of words 
        var datasetGerman = ctx.data("german");//Number of words 
        var datasetKA = ctx.data("na");//Number of words 
        var datatype = ctx.data("type");//Number of words 
        var myChart = new Chart(ctx, {
            type: datatype,
            data: {
                labels: arrayxbase,
                datasets: [{
                    data: datasetML,
                    label: "multilingual",
                    borderColor: "#3e95cd",
                    fill: false
                }, {
                    data: datasetGerman,
                    label: "German",
                    borderColor: "#ff6384",
                    fill: false
                }, {
                    data: datasetKA,
                    label: "NA",
                    borderColor: "#f6a828",
                    fill: false
                }
                ]
            }
        });
    });
});

/****************************************
Chart
/****************************************/



//    var minval=parseFloat($('#lemma-freq-slider').data( "min" )) ;
//    var maxval=parseFloat($('#lemma-freq-slider').data( "max" ) );



//       // --------------LEMMA---------------
//        $( "#lemma-freq-slider" ).slider({
//           range:true,
//           min: minval,
//           max: maxval,
//           values: [minval,maxval],
//           slide: function( event, ui ) {
//              $( "#lemma-freq-label" ).val(  ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//              $( "#id_min_lemma_freq" ).val( ui.values[ 0 ] );
//              $( "#id_max_lemma_freq" ).val( ui.values[ 1 ] );
//           }
//        });
//        $( "#lemma-freq-label" ).val( $( "#lemma-freq-slider" ).slider( "values", 0 ) +
//           " - " + $( "#lemma-freq-slider" ).slider( "values", 1 ) );

//    minval=parseFloat($('#lemma-absolute-slider').data( "min" )) ;
//    maxval=parseFloat($('#lemma-absolute-slider').data( "max" ) );
//       $( "#lemma-absolute-slider" ).slider({
//          range:true,
//          min: minval,
//          max: maxval,
//          values: [minval,maxval],
//          slide: function( event, ui ) {
//             $( "#lemma-absolute-label" ).val(  ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//             $( "#id_min_lemma_absolute" ).val( ui.values[ 0 ] );
//             $( "#id_max_lemma_absolute" ).val( ui.values[ 1 ] );
//          }
//       });


//       $( "#lemma-absolute-label" ).val(  "" + $( "#lemma-absolute-slider" ).slider( "values", 0 ) +
//          " - " + $( "#lemma-absolute-slider" ).slider( "values", 1 ) );
//          minval=parseFloat($('#lemma-Zipf-slider').data( "min" )) ;
//          maxval=parseFloat($('#lemma-Zipf-slider').data( "max" ) );
//          $( "#lemma-Zipf-slider" ).slider({
//           range:true,
//           min: minval,
//           max: maxval,
//           values: [minval,maxval],
//           slide: function( event, ui ) {
//              $( "#lemma-Zipf-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//              $( "#id_min_lemma_Zipf" ).val( ui.values[ 0 ] );
//              $( "#id_max_lemma_Zipf" ).val( ui.values[ 1 ] );
//           }
//        });
//        $( "#lemma-Zipf-label" ).val(  "" + $( "#lemma-Zipf-slider" ).slider( "values", 0 ) +
//           " - " + $( "#lemma-Zipf-slider" ).slider( "values", 1 ) );

//       // --------------Word---------------
//       minval=parseFloat($('#word-phonemes-slider').data( "min" )) ;
//       maxval=parseFloat($('#word-phonemes-slider').data( "max" ) );

//       $( "#word-phonemes-slider" ).slider({
//         range:true,
//         min: minval,
//         max: maxval,
//         values: [minval,maxval],
//         slide: function( event, ui ) {
//            $( "#word-phonemes-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//            $( "#id_min_word_phonemes" ).val( ui.values[ 0 ] );
//            $( "#id_max_word_phonemes" ).val( ui.values[ 1 ] );
//         }
//      });

//      $( "#word-phonemes-label" ).val(  "" + $( "#word-phonemes-slider" ).slider( "values", 0 ) +
//         " - " + $( "#word-phonemes-slider" ).slider( "values", 1 ) );

//         minval=parseFloat($('#word-graphemes-slider').data( "min" )) ;
//         maxval=parseFloat($('#word-graphemes-slider').data( "max" ) );
//         $( "#word-graphemes-slider" ).slider({
//           range:true,
//           min: minval,
//          max: maxval,
//          values: [minval,maxval],
//          slide: function( event, ui ) {
//              $( "#word-graphemes-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//              $( "#id_min_word_graphemes" ).val( ui.values[ 0 ] );
//              $( "#id_max_word_graphemes" ).val( ui.values[ 1 ] );
//           }
//        });

//        $( "#word-graphemes-label" ).val(  "" + $( "#word-graphemes-slider" ).slider( "values", 0 ) +
//           " - " + $( "#word-graphemes-slider" ).slider( "values", 1 ) );

//           minval=parseFloat($('#word-syllables-slider').data( "min" )) ;
//           maxval=parseFloat($('#word-syllables-slider').data( "max" ) );
//           $( "#word-syllables-slider" ).slider({
//             range:true,
//             min: minval,
//          max: maxval,
//          values: [minval,maxval],
//          slide: function( event, ui ) {
//                $( "#word-syllables-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                $( "#id_min_word_syllables" ).val( ui.values[ 0 ] );
//                $( "#id_max_word_syllables" ).val( ui.values[ 1 ] );
//             }
//          });

//          $( "#word-syllables-label" ).val(  "" + $( "#word-syllables-slider" ).slider( "values", 0 ) +
//             " - " + $( "#word-syllables-slider" ).slider( "values", 1 ) );
//             minval=parseFloat($('#word-morphemes-slider').data( "min" )) ;
//             maxval=parseFloat($('#word-morphemes-slider').data( "max" ) );

//             $( "#word-morphemes-slider" ).slider({
//               range:true,
//               min: minval,
//               max: maxval,
//          values: [minval,maxval],
//               slide: function( event, ui ) {
//                  $( "#word-morphemes-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                  $( "#id_min_word_morphemes" ).val( ui.values[ 0 ] );
//                  $( "#id_max_word_morphemes" ).val( ui.values[ 1 ] );
//               }
//            });

//            $( "#word-morphemes-label" ).val(  "" + $( "#word-morphemes-slider" ).slider( "values", 0 ) +
//               " - " + $( "#word-morphemes-slider" ).slider( "values", 1 ) );

//               minval=parseFloat($('#word-absolute-slider').data( "min" )) ;
//               maxval=parseFloat($('#word-absolute-slider').data( "max" ) );

//               $( "#word-absolute-slider" ).slider({
//                 range:true,
//                 min: minval,
//                 max: maxval,
//          values: [minval,maxval],
//                 slide: function( event, ui ) {
//                    $( "#word-absolute-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                    $( "#id_min_word_absolute" ).val( ui.values[ 0 ] );
//                    $( "#id_max_word_absolute" ).val( ui.values[ 1 ] );
//                 }
//              });
//              $( "#word-absolute-label" ).val(  "" + $( "#word-absolute-slider" ).slider( "values", 0 ) +
//                 " - " + $( "#word-absolute-slider" ).slider( "values", 1 ) );

//                 minval=parseFloat($('#word-freq-slider').data( "min" )) ;
//                 maxval=parseFloat($('#word-freq-slider').data( "max" ) );
//                 $( "#word-freq-slider" ).slider({
//                   range:true,
//                   min: minval,
//                   max: maxval,
//          values: [minval,maxval],
//                   slide: function( event, ui ) {
//                      $( "#word-freq-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                      $( "#id_min_word_freq" ).val( ui.values[ 0 ] );
//                      $( "#id_max_word_freq" ).val( ui.values[ 1 ] );
//                   }
//                });
//                $( "#word-freq-label" ).val(  "" + $( "#word-freq-slider" ).slider( "values", 0 ) +
//                   " - " + $( "#word-freq-slider" ).slider( "values", 1 ) );
//                   minval=parseFloat($('#word-bigram-slider').data( "min" )) ;
//                   maxval=parseFloat($('#word-bigram-slider').data( "max" ) );

//                   $( "#word-bigram-slider" ).slider({
//                     range:true,
//                     min: minval,
//                     max: maxval,
//                     values: [minval,maxval],
//                     slide: function( event, ui ) {
//                        $( "#word-bigram-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                        $( "#id_min_word_bigram" ).val( ui.values[ 0 ] );
//                        $( "#id_max_word_bigram" ).val( ui.values[ 1 ] );
//                     }
//                  });
//                  $( "#word-bigram-label" ).val(  "" + $( "#word-bigram-slider" ).slider( "values", 0 ) +
//                     " - " + $( "#word-bigram-slider" ).slider( "values", 1 ) );
//                     minval=parseFloat($('#word-neighbors-slider').data( "min" )) ;
//                     maxval=parseFloat($('#word-neighbors-slider').data( "max" ) );

//                     $( "#word-neighbors-slider" ).slider({
//                       range:true,
//                       min: minval,
//                      max: maxval,
//                      values: [minval,maxval],
//                       slide: function( event, ui ) {
//                          $( "#word-neighbors-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                          $( "#id_min_word_neighbors" ).val( ui.values[ 0 ] );
//                          $( "#id_max_word_neighbors" ).val( ui.values[ 1 ] );
//                       }
//                    });
//                    $( "#word-neighbors-label" ).val(  "" + $( "#word-neighbors-slider" ).slider( "values", 0 ) +
//                       " - " + $( "#word-neighbors-slider" ).slider( "values", 1 ) );
//                       minval=parseFloat($('#word-OLD20-slider').data( "min" )) ;
//                       maxval=parseFloat($('#word-OLD20-slider').data( "max" ) );

//                       $( "#word-OLD20-slider" ).slider({
//                         range:true,
//                         min: minval,
//                         max: maxval,
//                         values: [minval,maxval],
//                         slide: function( event, ui ) {
//                            $( "#word-OLD20-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                            $( "#id_min_word_OLD20" ).val( ui.values[ 0 ] );
//                            $( "#id_max_word_OLD20" ).val( ui.values[ 1 ] );
//                         }
//                      });
//                      $( "#word-OLD20-label" ).val(  "" + $( "#word-OLD20-slider" ).slider( "values", 0 ) +
//                         " - " + $( "#word-OLD20-slider" ).slider( "values", 1 ) );

// /// new slider

//                         minval=parseFloat($('#Err-wordform-slider').data( "min" )) ;
//                         maxval=parseFloat($('#Err-wordform-slider').data( "max" ) );

//                         $( "#Err-wordform-slider" ).slider({
//                           range:true,
//                           min: minval,
//                           max: maxval,
//                           values: [minval,maxval],
//                           slide: function( event, ui ) {
//                              $( "#Err-wordform-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                              $( "#id_min_Err_wordform" ).val( ui.values[ 0 ] );
//                              $( "#id_max_Err_wordform" ).val( ui.values[ 1 ] );
//                           }
//                        });
//                        $( "#Err-wordform-label" ).val(  "" + $( "#Err-wordform-slider" ).slider( "values", 0 ) +
//                           " - " + $( "#Err-wordform-slider" ).slider( "values", 1 ) );


//                         minval=parseFloat($('#Err-child-slider').data( "min" )) ;
//                         maxval=parseFloat($('#Err-child-slider').data( "max" ) );

//                         $( "#Err-child-slider" ).slider({
//                           range:true,
//                           min: minval,
//                           max: maxval,
//                           values: [minval,maxval],
//                           slide: function( event, ui ) {
//                              $( "#Err-child-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                              $( "#id_min_Err_child" ).val( ui.values[ 0 ] );
//                              $( "#id_max_Err_child" ).val( ui.values[ 1 ] );
//                           }
//                        });
//                        $( "#Err-child-label" ).val(  "" + $( "#Err-child-slider" ).slider( "values", 0 ) +
//                           " - " + $( "#Err-child-slider" ).slider( "values", 1 ) );



//                           minval=parseFloat($('#Err-spelling-slider').data( "min" )) ;
//                           maxval=parseFloat($('#Err-spelling-slider').data( "max" ) );

//                           $( "#Err-spelling-slider" ).slider({
//                             range:true,
//                             min: minval,
//                             max: maxval,
//                             values: [minval,maxval],
//                             slide: function( event, ui ) {
//                                $( "#Err-spelling-label" ).val(  "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//                                $( "#id_min_spelling_child" ).val( ui.values[ 0 ] );
//                                $( "#id_max_spelling_child" ).val( ui.values[ 1 ] );
//                             }
//                          });
//                          $( "#Err-spelling-label" ).val(  "" + $( "#Err-spelling-slider" ).slider( "values", 0 ) +
//                             " - " + $( "#Err-spelling-slider" ).slider( "values", 1 ) );