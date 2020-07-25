// https://www.tutorialspoint.com/jqueryui/jqueryui_slider.htm
$(function() {
      // --------------LEMMA---------------
       $( "#lemma-freq-slider" ).slider({
          range:true,
          min: 0,
          max: 500,
          values: [ 35, 200 ],
          slide: function( event, ui ) {
             $( "#lemma-freq-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
          }
       });
       $( "#lemma-freq-label" ).val( "$" + $( "#lemma-freq-slider" ).slider( "values", 0 ) +
          " - $" + $( "#lemma-freq-slider" ).slider( "values", 1 ) );
   
      $( "#lemma-absolute-slider" ).slider({
         range:true,
         min: 0,
         max: 500,
         values: [ 35, 200 ],
         slide: function( event, ui ) {
            $( "#lemma-absolute-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
         }
      });
      $( "#lemma-absolute-label" ).val( "$" + $( "#lemma-absolute-slider" ).slider( "values", 0 ) +
         " - $" + $( "#lemma-absolute-slider" ).slider( "values", 1 ) );

         $( "#lemma-Zipf-slider" ).slider({
          range:true,
          min: 0,
          max: 500,
          values: [ 35, 200 ],
          slide: function( event, ui ) {
             $( "#lemma-Zipf-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
          }
       });
       $( "#lemma-Zipf-label" ).val( "$" + $( "#lemma-Zipf-slider" ).slider( "values", 0 ) +
          " - $" + $( "#lemma-Zipf-slider" ).slider( "values", 1 ) );

      // --------------Word---------------

      $( "#word-phonemes-slider" ).slider({
        range:true,
        min: 0,
        max: 500,
        values: [ 35, 200 ],
        slide: function( event, ui ) {
           $( "#word-phonemes-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
     });
     $( "#word-phonemes-label" ).val( "$" + $( "#word-phonemes-slider" ).slider( "values", 0 ) +
        " - $" + $( "#word-phonemes-slider" ).slider( "values", 1 ) );
 
        $( "#word-graphemes-slider" ).slider({
          range:true,
          min: 0,
          max: 500,
          values: [ 35, 200 ],
          slide: function( event, ui ) {
             $( "#word-graphemes-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
          }
       });
       $( "#word-graphemes-label" ).val( "$" + $( "#word-graphemes-slider" ).slider( "values", 0 ) +
          " - $" + $( "#word-graphemes-slider" ).slider( "values", 1 ) );


          $( "#word-syllables-slider" ).slider({
            range:true,
            min: 0,
            max: 500,
            values: [ 35, 200 ],
            slide: function( event, ui ) {
               $( "#word-syllables-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            }
         });
         $( "#word-syllables-label" ).val( "$" + $( "#word-syllables-slider" ).slider( "values", 0 ) +
            " - $" + $( "#word-syllables-slider" ).slider( "values", 1 ) );


            $( "#word-morphemes-slider" ).slider({
              range:true,
              min: 0,
              max: 500,
              values: [ 35, 200 ],
              slide: function( event, ui ) {
                 $( "#word-morphemes-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
              }
           });
           $( "#word-morphemes-label" ).val( "$" + $( "#word-morphemes-slider" ).slider( "values", 0 ) +
              " - $" + $( "#word-morphemes-slider" ).slider( "values", 1 ) );



              $( "#word-absolute-slider" ).slider({
                range:true,
                min: 0,
                max: 500,
                values: [ 35, 200 ],
                slide: function( event, ui ) {
                   $( "#word-absolute-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                }
             });
             $( "#word-absolute-label" ).val( "$" + $( "#word-absolute-slider" ).slider( "values", 0 ) +
                " - $" + $( "#word-absolute-slider" ).slider( "values", 1 ) );
  
  
                $( "#word-freq-slider" ).slider({
                  range:true,
                  min: 0,
                  max: 500,
                  values: [ 35, 200 ],
                  slide: function( event, ui ) {
                     $( "#word-freq-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                  }
               });
               $( "#word-freq-label" ).val( "$" + $( "#word-freq-slider" ).slider( "values", 0 ) +
                  " - $" + $( "#word-freq-slider" ).slider( "values", 1 ) );

                  $( "#word-bigram-slider" ).slider({
                    range:true,
                    min: 0,
                    max: 500,
                    values: [ 35, 200 ],
                    slide: function( event, ui ) {
                       $( "#word-bigram-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                    }
                 });
                 $( "#word-bigram-label" ).val( "$" + $( "#word-bigram-slider" ).slider( "values", 0 ) +
                    " - $" + $( "#word-bigram-slider" ).slider( "values", 1 ) );
  
                    $( "#word-neighbors-slider" ).slider({
                      range:true,
                      min: 0,
                      max: 500,
                      values: [ 35, 200 ],
                      slide: function( event, ui ) {
                         $( "#word-neighbors-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                      }
                   });
                   $( "#word-neighbors-label" ).val( "$" + $( "#word-neighbors-slider" ).slider( "values", 0 ) +
                      " - $" + $( "#word-neighbors-slider" ).slider( "values", 1 ) );
              
                      $( "#word-OLD20-slider" ).slider({
                        range:true,
                        min: 0,
                        max: 500,
                        values: [ 35, 200 ],
                        slide: function( event, ui ) {
                           $( "#word-OLD20-label" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                        }
                     });
                     $( "#word-OLD20-label" ).val( "$" + $( "#word-OLD20-slider" ).slider( "values", 0 ) +
                        " - $" + $( "#word-OLD20-slider" ).slider( "values", 1 ) );
                
                        $('select.multi').selectpicker();

                           
/****************************************
   *       Basic Table                   *
   ****************************************/
   
  ExportTable($('#Word_zero_config'),$('#Wordexport'));
  ExportTable($('#lemma_config'),$('#lemmaexport'));
  ExportTable($('#global_config'),$('#globalexport'));
  ExportTable($('#text_config'),$('#textexport'));

   $('#Word_zero_config').DataTable( );
$('#lemma_config').DataTable({searching: false});
$('#global_config').DataTable({searching: false});
$('#text_config').DataTable({searching: false});
/****************************************
   *       Basic Table                   *
   * $('table').dataTable({searching: false, paging: false, info: false});
For DataTables <1.10, use:

$('table').dataTable({bFilter: false, bInfo: false});
or using pure CSS:

.dataTables_filter, .dataTables_info { display: none; }
   ****************************************/
  function ExportTable(table,divId){
    var $myTable = table;
    // Run `tableExport()`
    $myTable.tableExport({formats: ["xlsx", "csv"],});
    // Detach the `buttons` html
    var $buttons = $myTable.find('caption').children().detach();
    // Append the buttons to an element of your choosing
    $buttons.appendTo(divId);
  }                           
});

