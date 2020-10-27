<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改材质名称</h3>
            <y-form
                    ref="goodtextureForm"
                    :model="goodtextureForm"
                    :rules="goodtextureRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="材质纤维大类:" prop="texture"
                                      
                                      
                        >



                            
                            
                                <y-input
                            
                            v-model="goodtextureForm.texture"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="材质纤维大类别名:" prop="texture_alias"
                                      
                                      
                        >



                            
                            
                                <y-input
                            
                            v-model="goodtextureForm.texture_alias"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="是否需要填写成分含量:" prop="filled_content"
                                      
                                      
                        >



                            
                            
                                <y-select
                            
                            v-model="goodtextureForm.filled_content"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="归属材质大类:" prop="parent_id"
                                      
                                      
                        >



                            
                            
                                <y-select
                            
                            v-model="goodtextureForm.parent_id"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col >
                      <el-row type="flex" justify="end">

                      <el-form-item>
                            <el-button @click="submit('goodtextureForm')" type="primary">提交</el-button>
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

    import { putGoodtexture, getGoodtexture } from "@/api/goodtexture"


    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                goodtextureForm: {},
                goodtextureRules: {
                
                
                
                
                
                
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getGoodtexture()
        },
        methods: {
            async getGoodtexture() {
                const res = await getGoodtexture(this.$route.query.id)
                this.goodtextureForm = res.data
            },

            async putGoodtexture() {
                await putGoodtexture(this.$route.query.id, this.goodtextureForm)
                this.$router.push({ path: "/goodtexture" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.goodtextureForm.check((valid) => {
                    if (valid) {
                        this.putGoodtexture()
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