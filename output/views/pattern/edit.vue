<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改pattern</h3>
            <y-form
                    ref="patternForm"
                    :model="patternForm"
                    :rules="patternRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="图案名称:" prop="name">



                            
                            
                                <y-input
                            
                            v-model="patternForm.name"
                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="图案图片:" prop="pic">



                            
                            
                                <y-upload-image
                            
                            v-model="patternForm.pic"
                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('patternForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putPattern, getPattern } from "@/api/pattern"


    
    
    
    
    
    
    

    export default {

        data() {
            return {
                patternForm: {},
                patternRules: {
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getPattern()
        },
        methods: {
            async getPattern() {
                const res = await getPattern(this.$route.query.id)
                this.patternForm = res.data
            },

            async putPattern() {
                await putPattern(this.$route.query.id, this.patternForm)
                this.$router.push({ path: "/pattern" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.patternForm.check((valid) => {
                    if (valid) {
                        this.putPattern()
                    } else {
                        return false
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