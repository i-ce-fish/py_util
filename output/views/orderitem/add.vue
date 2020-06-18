<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加orderitem</h3>
            <y-form
                    ref="orderitemForm"
                    :model="orderitemForm"
                    :rules="orderitemRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="产品id:" prop="good_id">

                            
                            
                            <y-input
                            
                                v-model="orderitemForm.good_id"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="数量:" prop="quantity">

                            
                            
                            <y-input
                            
                                v-model="orderitemForm.quantity"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="总价:" prop="total">

                            
                            
                            <y-input
                            
                                v-model="orderitemForm.total"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="所属订单:" prop="goodorder_id">

                            
                            
                            <y-input
                            
                                v-model="orderitemForm.goodorder_id"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('orderitemForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>
    import { addOrderitem } from "../../api/orderitem"

    
    
    
    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                orderitemForm: {},
                orderitemRules: {
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addOrderitem() {
                await addOrderitem(this.orderitemForm)
                this.$router.push({ path: "/orderitem" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.orderitemForm.check((valid) => {
                    if (valid) {
                        this.addOrderitem()
                    } else {
                        return false
                    }
                    return undefined
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