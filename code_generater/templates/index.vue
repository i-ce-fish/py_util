<template>
    <div class="app-container">
      <el-card>
        <y-form
                ref="{{ModelNameSingular}}Form"
                :model="{{ModelNameSingular}}Form"
                label-width="80px"
        >

            {#  没有搜索条件的情况未考虑#}
            {% for Field in Fields%}
            {% if Field.Searchable %}
                    <el-row>

                        {% for Field in Fields%}
                        {% if Field.Searchable %}
                        <el-col :span="6">
                            <el-form-item label="{{Field.FieldNameCn}}:" prop="{{Field.FieldNameEn}}">

                                <{{ Field.VueComponent }}

                                v-model="{{ModelNameSingular}}Form.{{Field.FieldNameEn}}"
                                {#  判断Field.SelectAPi长度不为0就添加api属性  #}
                                {% if Field.SelectApi|trim|length != 0  %} api="{{Field.SelectApi}}" {% endif %}
                                {#  判断Field.Editable 是否可编辑 #}
                                {% if not Field.Editable  %}  disabled  {% endif %}
                                {#  判断Field.VueComponentConfig 自定义配置 #}
                                {% if Field.VueComponentConfig|trim|length != 0  %}  {{Field.VueComponentConfig}}  {% endif %}

                                {#  判断有没有上方提示  #}
                                {% if  Field.VueFormTips %}
                                tips="{{Field.VueFormTips}}"
                                {% endif %}

                                />
                            </el-form-item>
                        </el-col>
                        {% endif %}
                        {% endfor %}

                    </el-row>

            {% break %}
            {% endif %}
            {% endfor %}

          <el-row type="flex" align="space-between">
            <el-col>
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button @click="reset" class="y-mr-l-10">重置</el-button>
            </el-col>
            <el-button type="success" @click="add">添加{{ModuleNameCn}}</el-button>

          </el-row>
        </y-form>
      </el-card>
        <y-table
            :data="{{ModelNamePlural}}Data"
            :pagination="pagination"
            @sortBy="sortBy"
            @changePage4List="getList"
            class="y-p-t-20"
        >
            <template>

                {% for Field in Fields %}
                    {% if Field.VueShowinList %}
                        <el-table-column prop="{{Field.FieldNameEn}}"
                                         label="{{Field.FieldNameCn}}"
                                         align="center"
                                         {% if Field.Orderable %} sortable="{{Field.FieldNameEn}}" {% endif %}
                                         {% if Field.VueListWidth|trim|length != 0 %} width="{{Field.VueListWidth}}" {% endif %}
                                         {% if Field.VueListConfig|trim|length != 0 %}  {{Field.VueListConfig}}  {% endif %} >


                        </el-table-column>
                    {% endif %}
                {% endfor %}



                <el-table-column label="操作" width="100px"  align="center">
                    <template slot-scope="{row}">
                        <el-button type="text" size="small" @click="edit(row.id)">修改</el-button>
                      <el-divider direction="vertical"></el-divider>
                      <el-button type="text" size="small" @click="del(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </template>
        </y-table>
    </div>
</template>
<script>
    import {get{{ModelNamePlural|title}}, del{{ModelNameSingular|title}}} from "@/api/{{ModelNameSingular}}"

    export default {
        data() {
            return {
            {{ModelNameSingular}}Form: {},
            {{ModelNamePlural}}Data: [],
                pagination: {
                pageNumber: 1,
                    pageSize: 10
            },
            {#  搜索条件不表单校验、必填校验 {{ModelNameSingular}}Rules: {} #}
        }
        },
        created() {
            this.getList()
        },
        methods: {
            async getList(param) {
                const {data} = await get{{ModelNamePlural|title}}(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.{{ModelNamePlural}}Data = data.list
                this.pagination.total = data.pagination.total
            },

            add() {
                this.$router.push({path: "add"})
            },
            edit(id) {
                this.$router.push({path: "edit", query: {id}})
            },
            del(id) {
                this.$confirm("是否删除?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning"
                })
                    .then(() =>
                        del{{ModelNameSingular|title}}(id)
                    )
                    .then((response) => {
                        this.$message({
                          type: "success",
                          message: "删除成功!"
                        })
                        this.getList()
                      })
                    .catch(() => {
                        this.$message({
                            type: "info",
                            message: "已取消删除"
                        })
                    })
            },
            onSearch(sort) {
                this.getList({...this.{{ModelNameSingular}}Form, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.{{ModelNameSingular}}Form = {}
                this.getList()
            }
        }
    }
</script>

<style lang='scss' scoped>
.app-container {

}
</style>
