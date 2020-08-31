<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加goodsize</h3>
            <y-form
                    ref="goodsizeForm"
                    :model="goodsizeForm"
                    :rules="goodsizeRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="尺码名:" prop="size_name">





                          
                            
                            <y-input
                            
                                v-model="goodsizeForm.size_name"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="尺寸显示名:" prop="display_name">





                          
                            
                            <y-input
                            
                                v-model="goodsizeForm.display_name"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="尺寸解释:" prop="description">





                          
                            
                            <y-input
                            
                                v-model="goodsizeForm.description"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="ColorID:" prop="color_id">





                          
                            
                            <y-select
                            
                                v-model="goodsizeForm.color_id"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="库存数量:" prop="inventory">





                          
                            
                            <y-input
                            
                                v-model="goodsizeForm.inventory"
                                
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="货品ID:" prop="good_id">





                          
                            
                            <y-select
                            
                                v-model="goodsizeForm.good_id"
                                
                                 api="/api/goods" 
                                
                                
                                
                                  valueName='id' labelName='product_name'  
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('goodsizeForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>
    import { addGoodsize } from "../../api/goodsize"

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                goodsizeForm: {},
                goodsizeRules: {
                    
                        
                        
                        size_name:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  60,
                                        message: "请输入长度小于60的尺码名",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        display_name:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  69,
                                        message: "请输入长度小于69的尺寸显示名",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        description:[

                            
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  255,
                                        message: "请输入长度小于255的尺寸解释",
                                        trigger: "blur"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                    
                        
                        
                    
                        
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                
                    
                    
                        good_idOptions:[],
                    
                
            }
        },
        created() {
        },
        methods: {
            async addGoodsize() {
                await addGoodsize(this.goodsizeForm)
                this.$router.push({ path: "/goodsize" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.goodsizeForm.check((valid) => {
                    if (valid) {
                        this.addGoodsize()
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