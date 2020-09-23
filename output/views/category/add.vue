<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加商品分类</h3>
            <y-form
                    ref="categoryForm"
                    :model="categoryForm"
                    :rules="categoryRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="类别名:" prop="name">





                          
                            
                            <y-input
                            
                                v-model="categoryForm.name"
                                
                                

                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="排序:" prop="sort">





                          
                            
                            <y-input
                            
                                v-model="categoryForm.sort"
                                
                                

                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="父ID:" prop="parent_id">





                          
                            
                            <y-select
                            
                                v-model="categoryForm.parent_id"
                                
                                

                                
                                 api="/api/categories" 
                                
                                
                                
                                  labelName="catalog_name"
    valueName="id"  
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col>
                      <el-row type="flex" justify="end">
                        <el-form-item>
                              <el-button @click="submit('categoryForm')">提交</el-button>
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
    import { addCategory } from "@/api/category"

    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                categoryForm: {},
                categoryRules: {
                    
                        
                        
                        name:[

                            
                            
                                {required:true,
                                message:'请输入类别名',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的类别名",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        sort:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的排序",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                        parent_idOptions:[],
                    
                
            }
        },
        created() {
        },
        methods: {
            async addCategory() {
                await addCategory(this.categoryForm)
                this.$router.push({ path: "/category" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.categoryForm.check((valid) => {
                    if (valid) {
                        this.addCategory()
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