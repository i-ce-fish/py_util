<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改供货商及订货</h3>
            <y-form
                    ref="supplierinfoForm"
                    :model="supplierinfoForm"
                    :rules="supplierinfoRules"
                    label-width="100px"
            >
                <el-row :gutter="20">
                    
                    <el-col :span="12">
                        <el-form-item label="货品货源:" prop="supply_source"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierinfoForm.supply_source"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供应商录入日期:" prop="create_at"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierinfoForm.create_at"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货商编码:" prop="supplier_code"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierinfoForm.supplier_code"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货品牌:" prop="supply_brand"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierinfoForm.supply_brand"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="可授权品牌:" prop="authorized_brand"
                                      
                                      
                        >



                            
                                <y-radio
                            v-model="supplierinfoForm.authorized_brand"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="品质档次:" prop="brand_level"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierinfoForm.brand_level"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="性别:" prop="mg_gender"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierinfoForm.mg_gender"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="系列:" prop="mg_series"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierinfoForm.mg_series"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="品类:" prop="mg_category"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierinfoForm.mg_category"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="适穿年龄:" prop="mg_age"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierinfoForm.mg_age"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="基本风格:" prop="mg_style"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierinfoForm.mg_style"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="备忘:" prop="mg_memo"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierinfoForm.mg_memo"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="性价比:" prop="cost_performance"
                                      
                                      
                        >



                            
                                <y-radio
                            v-model="supplierinfoForm.cost_performance"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="起批方式:" prop="wholesale_mode"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierinfoForm.wholesale_mode"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="账期:" prop="account_period"
                                      
                                      
                        >



                            
                                <y-radio
                            v-model="supplierinfoForm.account_period"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="能否退货:" prop="refundable"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierinfoForm.refundable"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="商家靠谱度:" prop="good_reliable"
                                      
                                      
                        >



                            
                                <y-radio
                            v-model="supplierinfoForm.good_reliable"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="货品靠谱度:" prop="merchant_reliable"
                                      
                                      
                        >



                            
                                <y-radio
                            v-model="supplierinfoForm.merchant_reliable"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col >
                      <el-row type="flex" justify="end">

                      <el-form-item>
                            <el-button @click="submit('supplierinfoForm')" type="primary">提交</el-button>
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

    import { putSupplierinfo, getSupplierinfo } from "@/api/supplierinfo"


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                supplierinfoForm: {},
                supplierinfoRules: {
                
                
                
                supply_source:[

                    
                
                {required:true,
                    message:'请输入货品货源',
                    trigger:'blur'},
                

                
                

                
                
            ],
                
                
                
                
                
                
                
                supplier_code:[

                    
                
                {required:true,
                    message:'请输入供货商编码',
                    trigger:'blur'},
                

                
                

                
                
            ],
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getSupplierinfo()
        },
        methods: {
            async getSupplierinfo() {
                const res = await getSupplierinfo(this.$route.query.id)
                this.supplierinfoForm = res.data
            },

            async putSupplierinfo() {
                await putSupplierinfo(this.$route.query.id, this.supplierinfoForm)
                this.$router.push({ path: "/supplierinfo" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.supplierinfoForm.check((valid) => {
                    if (valid) {
                        this.putSupplierinfo()
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