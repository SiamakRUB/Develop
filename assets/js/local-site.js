
      /****************************************
         *       Basic Table                   *
         ****************************************/
$('#zero_config').DataTable();
/****************************************
   *       Basic Table                   *
   ****************************************/
var $body = $("body");
$('#btnsearch').on('click', function myfunction() {

    var ctx1 = document.getElementById('myChart1');
    var myChart1 = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: ['German', 'Other Country'],
            datasets: [{
                label: '# of Nationality',
                data: [42, 119],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)'

                ],

            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['German', 'Arabic', 'Turkish', 'Persian', 'Russian'],
            datasets: [{
                label: '# of Nationality',
                data: [12, 9, 3, 8, 2],
                backgroundColor: [
                    'rgba(255, 99, 132 )',
                    'rgba(54, 162, 235 )',
                    'rgba(255, 206, 86 )',
                    'rgba(75, 192, 192 )',
                    'rgba(126, 255, 60 )',
                    'rgba(153, 102, 25 )'

                ],

            }]
        }

    });
    var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

    new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
            labels: MONTHS,
            datasets: [{
                data: [86, 91, 106, 106, 107, 91, 85, 85, 52, 124],
                label: "Freq1",
                borderColor: "#3e95cd",
                fill: false
            }, {
                data: [107, 104, 103, 89, 95, 78, 89, 56, 41, 46],
                label: "Freq2",
                borderColor: "#ff6384",
                fill: false
            }
            ]
        },
        options: {
            title: {
                display: true,
                text: 'Progress of Frequency of this word in all text'
            }
        }
    });
    new Chart(document.getElementById("bar-chart-horizontal"), {
        type: 'horizontalBar',
        data: {
            labels: ["Grade 1 ", "Grade 2", "Grade 3", "Grade 4"],
            datasets: [
                {
                    label: "Population (millions)",
                    backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                    data: [2478, 5267, 734, 1784]
                }
            ]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Chart base on grade of students'
            }
        }
    });
    $('.container-search').toggleClass('hide');

});
function myfunction() {
}
$(".doexpand").on('click', function myfunction() {
    var $this = $(this).closest('td').next();
    var $table = $('.tbldetails').clone();
    if (!$this.hasClass('expand')) {

        $this.append($table);
    } else {
        var $tbl = $this.find('.tbldetails');
        $tbl.toggleClass('hide');
        $tbl.remove();
    }
    $this.toggleClass('expand');

    $table.toggleClass('hide');

    //$('.expand::after').toggle();
})

$("#basetype").on('change', function () {
    if (this.value == 1) {
        $("#pnltypeshow").fadeOut();
        $("#pnltokenshow").fadeIn();
    } else {
        $("#pnltokenshow").fadeOut();
        $("#pnltypeshow").fadeIn();
    }
    //$('.scale-changeble').toggleClass('col-md-6')
});

$(document).on({
    ajaxStart: function () { $body.addClass("loading"); },
    ajaxStop: function () { $body.removeClass("loading"); }
});