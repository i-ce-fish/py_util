<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改address</h3>
            <y-form
                    ref="addressForm"
                    :model="addressForm"
                    :rules="addressRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="省:" prop="province">

                            
                            
                                <y-input
                            
                            v-model="addressForm.province"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="市:" prop="city">

                            
                            
                                <y-input
                            
                            v-model="addressForm.city"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="详细地址:" prop="detail">

                            
                            
                                <y-input
                            
                            v-model="addressForm.detail"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="所属客户:" prop="customer_id">

                            
                            
                                <y-input
                            
                            v-model="addressForm.customer_id"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="是否为默认地址:" prop="is_default">

                            
                            
                                <y-radio
                            
                            v-model="addressForm.is_default"
                            
                            
                            
                            
                            
                              :options="[{value: 1,label: '是'},{value: 0,label: '否'}]"  

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('addressForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putAddress, getAddress } from "../../api/address"


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                addressForm: {},
                addressRules: {
                
                
                
                province:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  60,
                    message: "请输入长度小于60的省",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                city:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  60,
                    message: "请输入长度小于60的市",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                detail:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的详细地址",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getAddress()
        },
        methods: {
            async getAddress() {
                const res = await getAddress(this.$route.query.id)
                this.addressForm = res.data
            },

            async putAddress() {
                await putAddress(this.$route.query.id, this.addressForm)
                this.$router.push({ path: "/address" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit(addressForm) {
                this.$refs.addressForm.check((valid) => {
                    if (valid) {
                        this.putAddress()
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