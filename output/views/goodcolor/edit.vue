<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改goodcolor</h3>
            <y-form
                    ref="goodcolorForm"
                    :model="goodcolorForm"
                    :rules="goodcolorRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="颜色名字:" prop="color_name">

                            
                            
                                <y-input
                            
                            v-model="goodcolorForm.color_name"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="颜色缩略图:" prop="color_thumbnail">

                            
                            
                                <y-input
                            
                            v-model="goodcolorForm.color_thumbnail"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="图片缩略图:" prop="product_thumbnail">

                            
                            
                                <y-input
                            
                            v-model="goodcolorForm.product_thumbnail"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="GoodId:" prop="good_id">

                            
                            
                                <y-select
                            
                            v-model="goodcolorForm.good_id"
                            
                             api="/api/todo" 
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('goodcolorForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putGoodcolor, getGoodcolor } from "../../api/goodcolor"


    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                goodcolorForm: {},
                goodcolorRules: {
                
                
                
                color_name:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  60,
                    message: "请输入长度小于60的颜色名字",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                color_thumbnail:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的颜色缩略图",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                product_thumbnail:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的图片缩略图",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                        good_idOptions:[],
                    
                
        }
        },
        created() {
            this.getGoodcolor()
        },
        methods: {
            async getGoodcolor() {
                const res = await getGoodcolor(this.$route.query.id)
                this.goodcolorForm = res.data
            },

            async putGoodcolor() {
                await putGoodcolor(this.$route.query.id, this.goodcolorForm)
                this.$router.push({ path: "/goodcolor" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit(goodcolorForm) {
                this.$refs.goodcolorForm.check((valid) => {
                    if (valid) {
                        this.putGoodcolor()
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