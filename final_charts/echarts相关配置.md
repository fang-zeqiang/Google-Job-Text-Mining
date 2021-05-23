# 饼图

```javascript

option = {
    title: {
        text: '全球STEM领域职业需求',
        subtext: '以IT行业为例子',
        left: 'center',
        textStyle:{
            fontSize:30
        },
        subtextStyle:{
            fontSize:25
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)',
    },
    toolbox:{
        show:true,
        orient:"vertical",
        feature:{
            saveAsImage:{
                show:true,
            },
            restore:{
                show:true
            },
            dataView:{
                show:true
            }
        }
        
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['科学', '技术', '工程', '数学'],
        textStyle:{
            fontSize:25
        }
    },
    series: [
        {
            name: '职业需求',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
                {value: 155000, name: '科学'},
                {value: 200000, name: '技术'},
                {value: 190000, name: '工程'},
                {value: 144000, name: '数学'},
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        
        }
    ]
};

```

# 柱图

```javascript
var posList = [
    'left', 'right', 'top', 'bottom',
    'inside',
    'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
    'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
];

app.configParameters = {
    rotate: {
        min: -90,
        max: 90
    },
    align: {
        options: {
            left: 'left',
            center: 'center',
            right: 'right'
        }
    },
    verticalAlign: {
        options: {
            top: 'top',
            middle: 'middle',
            bottom: 'bottom'
        }
    },
    position: {
        options: echarts.util.reduce(posList, function (map, pos) {
            map[pos] = pos;
            return map;
        }, {})
    },
    distance: {
        min: 0,
        max: 100
    }
};

app.config = {
    rotate: 90,
    align: 'left',
    verticalAlign: 'middle',
    position: 'insideBottom',
    distance: 15,
    onChange: function () {
        var labelOption = {
            normal: {
                rotate: app.config.rotate,
                align: app.config.align,
                verticalAlign: app.config.verticalAlign,
                position: app.config.position,
                distance: app.config.distance
            }
        };
        myChart.setOption({
            series: [{
                label: labelOption
            }, {
                label: labelOption
            }, {
                label: labelOption
            }, {
                label: labelOption
            }]
        });
    }
};


var labelOption = {
    show: true,
    position: app.config.position,
    distance: app.config.distance,
    align: app.config.align,
    verticalAlign: app.config.verticalAlign,
    rotate: app.config.rotate,
    formatter: '{c}  {name|{a}}',
    fontSize: 16,
    rich: {
        name: {
            textBorderColor: '#fff'
        }
    }
};

option = {
 title: {
        text: '全球STEM各行业热门需求',
        left:"auto",
        top:"auto",
        textStyle:{
            fontSize:30
        },
        subtextStyle:{
            fontSize:25
        }
    },
    color: ['#003366', '#006699', '#4cabce', '#e5323e'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['科学', '技术', '工程', '数学'],
        textStyle: {fontSize : 25}
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {show: false},
            data: ['自动驾驶', "模式识别", '自然语言处理', "区块链", '软件开发'],
            axisLabel:{
                fontSize:18
            }
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: '科学',
            type: 'bar',
            barGap: 0,
            label: labelOption,
            data: [2400, 2320, 2610, 2740, 2500]
        },
        {
            name: '技术',
            type: 'bar',
            label: labelOption,
            data: [2200, 1820, 1910, 2340, 2600]
        },
        {
            name: '工程',
            type: 'bar',
            label: labelOption,
            data: [1500, 2320, 2010, 1540, 1900]
        },
        {
            name: '数学',
            type: 'bar',
            label: labelOption,
            data: [980, 1700, 1001, 990, 940]
        }
    ]
};;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
       </script>
   </body>
</html>

```

# 线图

```javascript

```

# 桑基图

```javascript

```

# 地理热点图

```javascript

```