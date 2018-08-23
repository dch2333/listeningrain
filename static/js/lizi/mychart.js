$(function(){
    //$()=window.onload=jQuery(document).ready()=$().ready()






    var data = [
        { label: "苹果",  data: 10},
        { label: "香蕉",  data: 30},
        { label: "西瓜",  data: 90},
        { label: "葡萄",  data: 70},
        { label: "柑橘",  data: 80},
        { label: "菠萝",  data: 110}
    ];
    fn_charts(data);


    var vData = [[1, 103], [2, 28], [3, 135], [4, 130], [5, 145], [6, 155], [7, 155], [8, 155], [9, 155], [10, 155], [11, 155], [12, 155]];
    fn_lineChart(vData);

    var data_h = [
               { label: "Bar", data: [ [1, 13], [2, 11], [3, 7] ] }
           ];
    fn_histogram(data_h);
});
/*折线图*/
var fn_lineChart = function(vData){
    //var vData = [[1, 103], [2, 28], [3, 135], [4, 130], [5, 145], [6, 155], [7, 155], [8, 155], [9, 155], [10, 155], [11, 155], [12, 155]];
    $.plot($("#placeholder"), [{ label: "", data: vData}],
            {
                series: { lines: { show: true }, points: { show: true} },
                xaxis: { ticks: [[1, "1月"], [3, "3月"], [5, "5月"], [7, "7月"], [9, "9月"], [11, "11月"]], min: 1, max: 12 },  //指定固定的显示内容
                yaxis: { ticks: 5, min: 0 }  //在y轴方向显示5个刻度，此时显示内容由 flot 根据所给的数据自动判断
            }
    );
}
var fn_charts = function(data){

    /*饼图1*/
        $.plot($("#pie1"), data, {
            series: {
                pie: {
                    show: true //显示饼图
                }
            },
            legend: {
                show: false //不显示图例
            }
        });
    /*饼图2*/
        $.plot($("#pie2"), data, {
            series: {             /*属性*/
                pie: {
                    show: true //显示饼图
                }
            }

        });
    /*饼图3*/
        $.plot($("#pie3"), data, {
            series: {
                pie: {
                    show: true,
                    radius: 1, //半径
                    label: {
                        show: true,
                        radius: 2/3,
                        formatter: function(label, series){
                            return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'+label+'<br/>'+Math.round(series.percent)+'%</div>';
                        },
                        threshold: 0.03  //这个值小于0.03，也就是3%时，label就会隐藏
                    }
                }
            },
            legend: {
                show: false
            }
        });
    /*饼图4*/
        $.plot($("#pie4"), data,
                {
                    series: {
                        pie: {
                            show: true
                        }
                    },
                    grid: {
                        hoverable: true,
                        clickable: true
                    }
                });

        $("#pie4").bind("plothover", pieHover);
        $("#pie4").bind("plotclick", pieClick);
}
function pieHover(event, pos, obj)
{
   if (!obj)
       return;
   percent = parseFloat(obj.series.percent).toFixed(2);
   $("#hover").html('<span style="font-weight: bold; color: '+obj.series.color+'">'+obj.series.label+' ('+percent+'%)</span>');
}

function pieClick(event, pos, obj)
{
   if (!obj)
       return;
   percent = parseFloat(obj.series.percent).toFixed(2);
   alert(''+obj.series.label+': '+percent+'%');
}

/*柱状图*/
var fn_histogram = function(data){

           var stack = 0, bars = true, lines = false, steps = false;

           $.plot($("#bar1"), data, {
               series: {
                   color: '#333',
                   abel: 'morris',
                   stack: 0,
                   lines: {
                       //show: true,
                       fill: true,
                       steps: false
                   },
                   point: {
                       show: true,
                   },
                   bars: {
                       show: true,
                       barWidth: 0.6
                   }
               }
           });
}
