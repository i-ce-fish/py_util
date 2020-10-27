<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改供货商及订货管理</h3>
            <y-form
                    ref="supplierorderForm"
                    :model="supplierorderForm"
                    :rules="supplierorderRules"
                    label-width="100px"
            >
                <el-row :gutter="20">
                    
                    <el-col :span="12">
                        <el-form-item label="供货货源:" prop="supply_source"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.supply_source"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供应商录入日期:" prop="joined_at"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierorderForm.joined_at"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货商编码:" prop="supplier_code"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierorderForm.supplier_code"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货品牌:" prop="supply_brand"
                                      
                                      
                        >



                            
                                <y-select
                            v-model="supplierorderForm.supply_brand"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="可授权品牌:" prop="authorized_brand"
                                      
                                      
                        >



                            
                                <y-radio
                            v-model="supplierorderForm.authorized_brand"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="品质档次:" prop="quality_level"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.quality_level"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货性别:" prop="supply_gender"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.supply_gender"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货系列:" prop="supply_series"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.supply_series"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货品类:" prop="supply_category"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.supply_category"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货年龄:" prop="supply_age"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.supply_age"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="供货风格:" prop="supply_style"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.supply_style"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="货品描述备忘录:" prop="good_memo"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierorderForm.good_memo"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="性价比:" prop="cost_performance"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.cost_performance"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="起批方式:" prop="wholesale_mode"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.wholesale_mode"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="账期:" prop="account_period"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.account_period"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="能否退货:" prop="refundable"
                                      
                                      
                        >



                            
                                <y-checkbox
                            v-model="supplierorderForm.refundable"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="商家靠谱程度:" prop="merchant_reliable"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierorderForm.merchant_reliable"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="货品靠谱程度:" prop="good_reliable"
                                      
                                      
                        >



                            
                                <y-input
                            v-model="supplierorderForm.good_reliable"

                          
                          

                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col >
                      <el-row type="flex" justify="end">

                      <el-form-item>
                            <el-button @click="submit('supplierorderForm')" type="primary">提交</el-button>
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

    import { putSupplierorder, getSupplierorder } from "@/api/supplierorder"


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                supplierorderForm: {},
                supplierorderRules: {
                
                
                
                
                
                
                
                
                
                supplier_code:[

                    
                
                {required:true,
                    message:'请输入供货商编码',
                    trigger:'blur'},
                

                
                

                
                
            ],
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getSupplierorder()
        },
        methods: {
            async getSupplierorder() {
                const res = await getSupplierorder(this.$route.query.id)
                this.supplierorderForm = res.data
            },

            async putSupplierorder() {
                await putSupplierorder(this.$route.query.id, this.supplierorderForm)
                this.$router.push({ path: "/supplierorder" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.supplierorderForm.check((valid) => {
                    if (valid) {
                        this.putSupplierorder()
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