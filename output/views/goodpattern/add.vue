<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加商品图案</h3>
            <y-form
                    ref="goodpatternForm"
                    :model="goodpatternForm"
                    :rules="goodpatternRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="图案名称:" prop="pattern_name"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodpatternForm.pattern_name"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="父级图案名称:" prop="parent_id"
                            
                            
                        >





                          
                            
                            <y-select
                            
                                v-model="goodpatternForm.parent_id"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col>
                      <el-row type="flex" justify="end">
                        <el-form-item>
                              <el-button @click="submit('goodpatternForm')">提交</el-button>
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
    import { addGoodpattern } from "@/api/goodpattern"

    
    
    
    
    
    
    


    export default {

        data() {
            return {
                goodpatternForm: {},
                goodpatternRules: {
                    
                        
                        
                    
                        
                        
                    
                },

                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addGoodpattern() {
                await addGoodpattern(this.goodpatternForm)
                this.$router.push({ path: "/goodpattern" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.goodpatternForm.check((valid) => {
                    if (valid) {
                        this.addGoodpattern()
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