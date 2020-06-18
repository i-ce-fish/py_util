<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改goodorder</h3>
            <y-form
                    ref="goodorderForm"
                    :model="goodorderForm"
                    :rules="goodorderRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="顾客ID:" prop="cusutomer_id">

                            
                            
                                <y-input
                            
                            v-model="goodorderForm.cusutomer_id"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="订单金额:" prop="total_amount">

                            
                            
                                <y-input
                            
                            v-model="goodorderForm.total_amount"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('goodorderForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putGoodorder, getGoodorder } from "../../api/goodorder"


    
    
    
    
    
    
    

    export default {

        data() {
            return {
                goodorderForm: {},
                goodorderRules: {
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getGoodorder()
        },
        methods: {
            async getGoodorder() {
                const res = await getGoodorder(this.$route.query.id)
                this.goodorderForm = res.data
            },

            async putGoodorder() {
                await putGoodorder(this.$route.query.id, this.goodorderForm)
                this.$router.push({ path: "/goodorder" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit(goodorderForm) {
                this.$refs.goodorderForm.check((valid) => {
                    if (valid) {
                        this.putGoodorder()
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