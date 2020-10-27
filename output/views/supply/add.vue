<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加supply</h3>
            <y-form
                    ref="supplyForm"
                    :model="supplyForm"
                    :rules="supplyRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="货源名称:" prop="supply">





                          
                            
                            <y-input
                            
                                v-model="supplyForm.supply"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="联系人:" prop="contact">





                          
                            
                            <y-input
                            
                                v-model="supplyForm.contact"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="联系电话:" prop="phone">





                          
                            
                            <y-input
                            
                                v-model="supplyForm.phone"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="进货地址:" prop="address">





                          
                            
                            <y-input
                            
                                v-model="supplyForm.address"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('supplyForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>
    import { addSupply } from "@/api/supply"

    
    
    
    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                supplyForm: {},
                supplyRules: {
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addSupply() {
                await addSupply(this.supplyForm)
                this.$router.push({ path: "/supply" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.supplyForm.check((valid) => {
                    if (valid) {
                        this.addSupply()
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