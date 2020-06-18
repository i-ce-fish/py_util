<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改customer</h3>
            <y-form
                    ref="customerForm"
                    :model="customerForm"
                    :rules="customerRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="顾客名称:" prop="name">

                            
                            
                                <y-input
                            
                            v-model="customerForm.name"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="微信号:" prop="wechat_id">

                            
                            
                                <y-input
                            
                            v-model="customerForm.wechat_id"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="顾客积分:" prop="credits">

                            
                            
                                <y-input
                            
                            v-model="customerForm.credits"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="默认地址ID:" prop="default_addr_id">

                            
                            
                                <y-select
                            
                            v-model="customerForm.default_addr_id"
                            
                             api="/api/todo" 
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="会员级别:" prop="vip_level">

                            
                            
                                <y-input
                            
                            v-model="customerForm.vip_level"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('customerForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putCustomer, getCustomer } from "../../api/customer"


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                customerForm: {},
                customerRules: {
                
                
                
                name:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  60,
                    message: "请输入长度小于60的顾客名称",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                wechat_id:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  60,
                    message: "请输入长度小于60的微信号",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                        default_addr_idOptions:[],
                    
                
                    
                        
                
        }
        },
        created() {
            this.getCustomer()
        },
        methods: {
            async getCustomer() {
                const res = await getCustomer(this.$route.query.id)
                this.customerForm = res.data
            },

            async putCustomer() {
                await putCustomer(this.$route.query.id, this.customerForm)
                this.$router.push({ path: "/customer" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit(customerForm) {
                this.$refs.customerForm.check((valid) => {
                    if (valid) {
                        this.putCustomer()
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