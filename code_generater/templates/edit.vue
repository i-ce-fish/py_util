<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改{{ModuleNameCn}}</h3>
            <y-form
                    ref="{{ModelNameSingular}}Form"
                    :model="{{ModelNameSingular}}Form"
                    :rules="{{ModelNameSingular}}Rules"
                    label-width="100px"
            >
                <el-row :gutter="20">
                    {% for Field in Fields%}
                    <el-col :span="12">
                        <el-form-item label="{{Field.FieldNameCn}}:" prop="{{Field.FieldNameEn}}"
                                      {# 表单域标签的宽度#}
                                      {% if  Field.FormLabelWidth %}
                                      label-width="{{Field.FormLabelWidth}}"
                                      {% endif %}
                        >



                            {#  判断Field.FieldType是否布尔类型，直接显示为单选框  #}
                                <{{ Field.VueComponent }}
                            v-model="{{ModelNameSingular}}Form.{{Field.FieldNameEn}}"

                          {# 提示符#}
                          {% if  Field.VueFormPlaceholder %}
                          placeholder="{{Field.VueFormPlaceholder}}"
                          {% endif %}

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
                    {% endfor %}

                    <el-col >
                      <el-row type="flex" justify="end">

                      <el-form-item>
                            <el-button @click="submit('{{ModelNameSingular}}Form')" type="primary">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                      </el-row>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { put{{ModelNameSingular|title}}, get{{ModelNameSingular|title}} } from "@/api/{{ModelNameSingular}}"


    {% for Field in Fields%}
    {#  判断是否有校验  #}
    {% if Field.VueRegx|trim|length != 0%}
    import { regular } from "../../utils/validate"
    {% break %}
    {% endif %}
    {% endfor %}

    export default {

        data() {
            return {
                {{ModelNameSingular}}Form: {},
                {{ModelNameSingular}}Rules: {
                {% for Field in Fields%}
                {#  判断是否有校验或者必填或者字符串长度限制  #}
                {% if Field.VueRegx|trim|length != 0   or Field.IsRequired or Field.FieldType|truncate(length=6,end='', leeway=0) == 'String'%}
                {{Field.FieldNameEn}}:[

                    {#  判断是否必填 #}
                {% if Field.IsRequired %}
                {required:true,
                    message:'请输入{{Field.FieldNameCn}}',
                    trigger:'blur'},
                {% endif %}

                {#  判断是否有string类型且有长度限制 ***truncate(保留长度，结尾，公差)源码/Lib/site-packages/filters/do_truncate #}
                {% if Field.FieldType|truncate(length=6,end='', leeway=0) == 'String' %}
                {# 替换字符串提取数字#}
                {
                    type: "string",
                        max:  {{Field.FieldType|replace('String','')|replace('(','')|replace(')','')}},
                    message: "请输入长度小于{{Field.FieldType|replace('String','')|replace('(','')|replace(')','')}}的{{Field.FieldNameCn}}",
                        trigger: "blur"
                },
                {% endif %}

                {#  判断是否有自定义校验 #}
                {% if Field.VueRegx %}
                {{Field.VueRegx}},
                {% endif %}
            ],
                {% endif %}
                {% endfor %}
            },

                {% for Field in Fields%}
                    {#  判断Field.SelectAPi长度不为0就添加options属性  #}
                        {% if Field.SelectApi|trim|length != 0  %}
                        {{Field.FieldNameEn}}Options:[],
                    {% endif %}
                {% endfor %}
        }
        },
        created() {
            this.get{{ModelNameSingular|title}}()
        },
        methods: {
            async get{{ModelNameSingular|title}}() {
                const res = await get{{ModelNameSingular|title}}(this.$route.query.id)
                this.{{ModelNameSingular}}Form = res.data
            },

            async put{{ModelNameSingular|title}}() {
                await put{{ModelNameSingular|title}}(this.$route.query.id, this.{{ModelNameSingular}}Form)
                this.$router.push({ path: "/{{ModelNameSingular}}" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.{{ModelNameSingular}}Form.check((valid) => {
                    if (valid) {
                        this.put{{ModelNameSingular|title}}()
                    }
                })
            }

        }

    }
</script>
<style lang='scss' scoped>
    .card-container {
        .box-card {

        }
    }
</style>
