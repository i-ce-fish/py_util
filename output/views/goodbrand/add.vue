<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加品牌名称</h3>
            <y-form
                    ref="goodbrandForm"
                    :model="goodbrandForm"
                    :rules="goodbrandRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="品牌中文名:" prop="brand_name"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodbrandForm.brand_name"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="品牌英文名:" prop="brand_eng"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodbrandForm.brand_eng"
                                
                                




                          
                                
                                
                                
                                
                                  placeholder='如果没有就不用填'  
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="品牌名称简写:" prop="brand_abbr"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodbrandForm.brand_abbr"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="品牌编码:" prop="fieldname"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodbrandForm.fieldname"
                                
                                




                          
                                
                                
                                
                                
                                  placeholder='请输入两位数字。示范: 66'  
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col>
                      <el-row type="flex" justify="end">
                        <el-form-item>
                              <el-button @click="submit('goodbrandForm')">提交</el-button>
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
    import { addGoodbrand } from "@/api/goodbrand"

    
    
    
    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                goodbrandForm: {},
                goodbrandRules: {
                    
                        
                        
                        brand_name:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的品牌中文名",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        brand_eng:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  45,
                                        message: "请输入长度小于45的品牌英文名",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        brand_abbr:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  45,
                                        message: "请输入长度小于45的品牌名称简写",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        fieldname:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  45,
                                        message: "请输入长度小于45的品牌编码",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addGoodbrand() {
                await addGoodbrand(this.goodbrandForm)
                this.$router.push({ path: "/goodbrand" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.goodbrandForm.check((valid) => {
                    if (valid) {
                        this.addGoodbrand()
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