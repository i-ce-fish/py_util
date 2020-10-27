<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加color</h3>
            <y-form
                    ref="colorForm"
                    :model="colorForm"
                    :rules="colorRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="颜色名称:" prop="color_name">





                          
                            
                            <y-input
                            
                                v-model="colorForm.color_name"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="色系:" prop="group">





                          
                            
                            <y-select
                            
                                v-model="colorForm.group"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="编码:" prop="code">





                          
                            
                            <y-input
                            
                                v-model="colorForm.code"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="颜色选择:" prop="code">





                          
                            
                            <y-input
                            
                                v-model="colorForm.code"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('colorForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>
    import { addColor } from "@/api/color"

    
    
    
    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                colorForm: {},
                colorRules: {
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addColor() {
                await addColor(this.colorForm)
                this.$router.push({ path: "/color" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.colorForm.check((valid) => {
                    if (valid) {
                        this.addColor()
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