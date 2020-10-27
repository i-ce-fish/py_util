<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加颜色名称</h3>
            <y-form
                    ref="color2Form"
                    :model="color2Form"
                    :rules="color2Rules"
                    label-width="100px"
            >
                <el-row :gutter="20">
                    
                    <el-col :span="12">
                        <el-form-item
                            label="颜色色系:" prop="color_system"
                            
                            
                        >





                          
                            
                            <y-select
                            
                                v-model="color2Form.color_system"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="色系编码范围:" prop="color_id_scope"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="color2Form.color_id_scope"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="颜色名称:" prop="color_name"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="color2Form.color_name"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col>
                      <el-row type="flex" justify="end">
                        <el-form-item>
                              <el-button @click="submit('color2Form')" type="primary">提交</el-button>
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
    import { addColor2 } from "@/api/color2"

    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                color2Form: {},
                color2Rules: {
                    
                        
                        
                        color_system:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的颜色色系",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        color_id_scope:[

                            
                            
                                {required:true,
                                message:'请输入色系编码范围',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的色系编码范围",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        color_name:[

                            
                            
                                {required:true,
                                message:'请输入颜色名称',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  60,
                                        message: "请输入长度小于60的颜色名称",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addColor2() {
                await addColor2(this.color2Form)
                this.$router.push({ path: "/color2" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.color2Form.check((valid) => {
                    if (valid) {
                        this.addColor2()
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