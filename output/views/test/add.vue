<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>添加测试模板</h3>
            <y-form
                    ref="testForm"
                    :model="testForm"
                    :rules="testRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="字段1:" prop="field1"
                            
                            
                            label-width="20px"
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="testForm.field1"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="字段2:" prop="field2"
                            
                            
                            label-width="120px"
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="testForm.field2"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item
                            label="字段2:" prop="field3"
                            
                            
                        >





                          
                            
                            <y-input
                            
                                v-model="testForm.field3"
                                
                                




                          
                                
                                
                                
                                
                                
                                
                                
                            />



                        </el-form-item>
                    </el-col>
                    

                    <el-col>
                      <el-row type="flex" justify="end">
                        <el-form-item>
                              <el-button @click="submit('testForm')">提交</el-button>
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
    import { addTest } from "@/api/test"

    
    
    
    
    
    
    
    
    
    


    export default {

        data() {
            return {
                testForm: {},
                testRules: {
                    
                        
                        
                        field1:[

                            
                            
                                {required:true,
                                message:'请输入字段1',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  60,
                                        message: "请输入长度小于60的字段1",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        field2:[

                            
                            
                                {required:true,
                                message:'请输入字段2',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  60,
                                        message: "请输入长度小于60的字段2",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                        
                        
                        field3:[

                            
                            
                                {required:true,
                                message:'请输入字段2',
                                trigger:'blur'},
                            

                            
                            
                                    
                                    {
                                        type: "string",
                                        max:  60,
                                        message: "请输入长度小于60的字段2",
                                        trigger: "change"
                                    },
                            

                            
                            
                        ],
                        
                    
                },

                
                    
                    
                
                    
                    
                
                    
                    
                
            }
        },
        created() {
        },
        methods: {
            async addTest() {
                await addTest(this.testForm)
                this.$router.push({ path: "/test" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.testForm.check((valid) => {
                    if (valid) {
                        this.addTest()
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