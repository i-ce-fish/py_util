<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加article</h3>
            <y-form
                    ref="articleForm"
                    :model="articleForm"
                    :rules="articleRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="标题:" prop="title">

                            
                            
                            <y-input
                            
                                v-model="articleForm.title"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="正文:" prop="body">

                            
                            
                            <y-input
                            
                                v-model="articleForm.body"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="封面图:" prop="front_pic">

                            
                            
                            <y-upload-single
                            
                                v-model="articleForm.front_pic"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="作者:" prop="author">

                            
                            
                            <y-input
                            
                                v-model="articleForm.author"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="是否首页:" prop="is_header">

                            
                            
                            <y-radio
                            
                                v-model="articleForm.is_header"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="是否头条:" prop="is_col_header">

                            
                            
                            <y-radio
                            
                                v-model="articleForm.is_col_header"
                                
                                
                                
                                
                                
                                

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="栏目ID:" prop="catalog_id">

                            
                            
                            <y-select
                            
                                v-model="articleForm.catalog_id"
                                
                                 api="/api/catalogs" 
                                
                                
                                
                                  labelName='catalog_name'  valueName='id'  

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="简介:" prop="intro">

                            
                            
                            <y-input
                            
                                v-model="articleForm.intro"
                                
                                
                                
                                
                                
                                  type="textarea"  

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('articleForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>
    import { addArticle } from "../../api/article"

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                articleForm: {},
                articleRules: {
                    
                        
                        
                        title:[

                            
                            
                                {required:true,
                                message:'请输入标题',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的标题",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                    
                        
                        
                        front_pic:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的封面图",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        author:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  80,
                                        message: "请输入长度小于80的作者",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                        
                        
                        intro:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的简介",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                        catalog_idOptions:[],
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addArticle() {
                await addArticle(this.articleForm)
                this.$router.push({ path: "/article" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.articleForm.check((valid) => {
                    if (valid) {
                        this.addArticle()
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