<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改catalog</h3>
            <y-form
                    ref="catalogForm"
                    :model="catalogForm"
                    :rules="catalogRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="类别名:" prop="catalog_name">

                          
                          
                          <el-tooltip  content="请输入图文分类名称 " placement="top-start">
                            

                            
                            
                                <y-input
                            
                            v-model="catalogForm.catalog_name"
                            
                            
                            
                            
                            
                            

                            />

                            
                            
                          </el-tooltip>
                          
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

    import { putCatalog, getCatalog } from "../../api/catalog"


    
    
    
    
    
    
    

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
            this.getCatalog()
        },
        methods: {
            async getCatalog() {
                const res = await getCatalog(this.$route.query.id)
                this.catalogForm = res.data
            },

            async putCatalog() {
                await putCatalog(this.$route.query.id, this.catalogForm)
                this.$router.push({ path: "/catalog" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.catalogForm.check((valid) => {
                    if (valid) {
                        this.putCatalog()
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