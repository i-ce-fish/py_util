<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加catalog</h3>
            <y-form
                    ref="catalogForm"
                    :model="catalogForm"
                    :rules="catalogRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="类别名:" prop="catalog_name">





                          
                            
                            <y-input
                            
                                v-model="catalogForm.catalog_name"
                                
                                
                                
                                
                                
                                
                                
                                
                                tips="请输入图文分类名称"
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="介绍:" prop="description">





                          
                            
                            <y-input
                            
                                v-model="catalogForm.description"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('catalogForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>
    import { addCatalog } from "../../api/catalog"

    
    
    
    
    
    
    


    export default {

        data() {
            return {
                catalogForm: {},
                catalogRules: {
                    
                        
                        
                        catalog_name:[

                            
                            
                                {required:true,
                                message:'请输入类别名',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的类别名",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        description:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的介绍",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                },

                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addCatalog() {
                await addCatalog(this.catalogForm)
                this.$router.push({ path: "/catalog" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.catalogForm.check((valid) => {
                    if (valid) {
                        this.addCatalog()
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