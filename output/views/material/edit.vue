<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改material</h3>
            <y-form
                    ref="materialForm"
                    :model="materialForm"
                    :rules="materialRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="材质名称:" prop="name">



                            
                            
                                <y-input
                            
                            v-model="materialForm.name"
                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="含量%:" prop="contain">



                            
                            
                                <y-upload-image
                            
                            v-model="materialForm.contain"
                            
                            
                            
                            
                            
                            
                            
                            
                            tips="0% ~ 100%"
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('materialForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putMaterial, getMaterial } from "@/api/material"


    
    
    
    
    
    
    

    export default {

        data() {
            return {
                materialForm: {},
                materialRules: {
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getMaterial()
        },
        methods: {
            async getMaterial() {
                const res = await getMaterial(this.$route.query.id)
                this.materialForm = res.data
            },

            async putMaterial() {
                await putMaterial(this.$route.query.id, this.materialForm)
                this.$router.push({ path: "/material" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.materialForm.check((valid) => {
                    if (valid) {
                        this.putMaterial()
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