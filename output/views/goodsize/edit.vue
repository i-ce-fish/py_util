<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改商品尺码</h3>
            <y-form
                    ref="goodsizeForm"
                    :model="goodsizeForm"
                    :rules="goodsizeRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="尺码名:" prop="size_name">



                            
                            
                                <y-input
                            
                            v-model="goodsizeForm.size_name"

                          
                          
                          placeholder="XS"
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="尺寸显示名:" prop="display_name">



                            
                            
                                <y-input
                            
                            v-model="goodsizeForm.display_name"

                          
                          
                          placeholder="160/84A/XS"
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="尺寸解释:" prop="description">



                            
                            
                                <y-input
                            
                            v-model="goodsizeForm.description"

                          
                          
                          placeholder="肩宽：50.5   身宽：52    后肩衣长72   连肩袖长：79.5"
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="尺码类别:" prop="size_type">



                            
                            
                                <y-select
                            
                            v-model="goodsizeForm.size_type"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col >
                      <el-row type="flex" justify="end">

                      <el-form-item>
                            <el-button @click="submit('goodsizeForm')">提交</el-button>
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

    import { putGoodsize, getGoodsize } from "@/api/goodsize"


    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                goodsizeForm: {},
                goodsizeRules: {
                
                
                
                size_name:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的尺码名",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                display_name:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  69,
                    message: "请输入长度小于69的尺寸显示名",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                description:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的尺寸解释",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                size_type:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  69,
                    message: "请输入长度小于69的尺码类别",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getGoodsize()
        },
        methods: {
            async getGoodsize() {
                const res = await getGoodsize(this.$route.query.id)
                this.goodsizeForm = res.data
            },

            async putGoodsize() {
                await putGoodsize(this.$route.query.id, this.goodsizeForm)
                this.$router.push({ path: "/goodsize" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.goodsizeForm.check((valid) => {
                    if (valid) {
                        this.putGoodsize()
                    }
                })
            }

        }

    }
</script>
<style lang='scss' scope>
    .card-container {
        background-color: #f0f2f5;
        padding: 30px;
        min-height: 100vh;

        .box-card {

        }
    }
</style>