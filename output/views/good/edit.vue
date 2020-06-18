<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改good</h3>
            <y-form
                    ref="goodForm"
                    :model="goodForm"
                    :rules="goodRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="商品名称:" prop="product_name">

                            
                            
                                <y-input
                            
                            v-model="goodForm.product_name"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="商品编号:" prop="product_sn">

                            
                            
                                <y-input
                            
                            v-model="goodForm.product_sn"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="款式编号:" prop="type_sn">

                            
                            
                                <y-input
                            
                            v-model="goodForm.type_sn"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="适合性别:" prop="gender">

                            
                            
                                <y-select
                            
                            v-model="goodForm.gender"
                            
                            
                            
                            
                            
                              :options="[{value: '1',label: '男'},{value: '0',label: '女'}]"  

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="材质:" prop="material">

                            
                            
                                <y-input
                            
                            v-model="goodForm.material"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="吊牌价格:" prop="original_price">

                            
                            
                                <y-input
                            
                            v-model="goodForm.original_price"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="优惠价格:" prop="onsale_price">

                            
                            
                                <y-input
                            
                            v-model="goodForm.onsale_price"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="vip价格:" prop="vip_price">

                            
                            
                                <y-input
                            
                            v-model="goodForm.vip_price"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="颜色:" prop="colors">

                            
                            
                                <y-input
                            
                            v-model="goodForm.colors"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="尺码:" prop="sizes">

                            
                            
                                <y-input
                            
                            v-model="goodForm.sizes"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="轮播图:" prop="carousels">

                            
                            
                                <y-upload-multiple
                            
                            v-model="goodForm.carousels"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="页面主图:" prop="main_pic">

                            
                            
                                <y-upload-single
                            
                            v-model="goodForm.main_pic"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="产品参数:" prop="produt_parameter">

                            
                            
                                <y-input
                            
                            v-model="goodForm.produt_parameter"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    
                    <el-col :span="12">
                        <el-form-item label="产品详情:" prop="detail">

                            
                            
                                <y-input
                            
                            v-model="goodForm.detail"
                            
                            
                            
                            
                            
                            

                            />
                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('goodForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putGood, getGood } from "../../api/good"


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    export default {

        data() {
            return {
                goodForm: {},
                goodRules: {
                
                
                
                product_name:[

                    
                
                {required:true,
                    message:'请输入商品名称',
                    trigger:'blur'},
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的商品名称",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                product_sn:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  80,
                    message: "请输入长度小于80的商品编号",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                type_sn:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  80,
                    message: "请输入长度小于80的款式编号",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                main_pic:[

                    
                

                
                
                
                {
                    type: "string",
                        max:  255,
                    message: "请输入长度小于255的页面主图",
                        trigger: "blur"
                },
                

                
                
            ],
                
                
                
                
                
                
                
                
            },

                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
                    
                        
                
        }
        },
        created() {
            this.getGood()
        },
        methods: {
            async getGood() {
                const res = await getGood(this.$route.query.id)
                this.goodForm = res.data
            },

            async putGood() {
                await putGood(this.$route.query.id, this.goodForm)
                this.$router.push({ path: "/good" })

                this.$message({
                    message: "添加成功",
                    type: "success"
                })
            },

            async submit(goodForm) {
                this.$refs.goodForm.check((valid) => {
                    if (valid) {
                        this.putGood()
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