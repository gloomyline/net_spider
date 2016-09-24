## instance of netSpider
1. 确定目标

    - 抓取百度百科python词条页面：标题和简介
    - 以及相关页面标题和简介
2. 分析目标(抓取网站的策略)

    - URL格式，限定抓取页面的范围
        > 目的：便面抓取不相干的网页，造成资源的浪费
        
        > 词条页面URL：/view/123.htm

    - 数据格式：分析词条页面中标题和简介所在的标签的格式

        - 标题：`<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>`
        - 简介：`<div class="lemma-summary" label-module="lemmaSummary">***</div>`
    - 网页编码：HTML解析器需要指定HTML编码 
        > 本实例是utf-8
    
    - mark:定向抓取网站爬虫的**抓取策略**根据目标网站实时更新
3. 编写代码
4. 执行爬虫