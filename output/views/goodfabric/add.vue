<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加面料名称</h3>
            <y-form
                    ref="goodfabricForm"
                    :model="goodfabricForm"
                    :rules="goodfabricRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="面料类别:" prop="category"
                            
                            
                        >





                          
                            
                            <y-select
                            
                                v-model="goodfabricForm.category"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="面料名称:" prop="name"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodfabricForm.name"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="面料别名:" prop="fabric_alias"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="goodfabricForm.fabric_alias"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col>
                      <el-row type="flex" justify="end">
                        <el-form-item>
                              <el-button @click="submit('goodfabricForm')" type="primary">提交</el-button>
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
    import { addGoodfabric } from "@/api/goodfabric"

    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                goodfabricForm: {},
                goodfabricRules: {
                    
                        
                        
                        category:[

                            
                            
                                {required:true,
                                message:'请输入面料类别',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的面料类别",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        name:[

                            
                            
                                {required:true,
                                message:'请输入面料名称',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的面料名称",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        fabric_alias:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的面料别名",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addGoodfabric() {
                await addGoodfabric(this.goodfabricForm)
                this.$router.push({ path: "/goodfabric" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.goodfabricForm.check((valid) => {
                    if (valid) {
                        this.addGoodfabric()
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