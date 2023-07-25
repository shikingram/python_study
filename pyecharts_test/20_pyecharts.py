from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts


line = Line()

line.add_xaxis(["kingram","anna","uzi"])

line.add_yaxis("kills",[1,2,3])

line.set_global_opts(
    title_opts = TitleOpts(title="kill展示",pos_left="center",pos_bottom="1%"),
    # legend_opts = LegendOpts(is_show = True),
    toolbox_opts= ToolboxOpts(is_show=True),
)

line.render()