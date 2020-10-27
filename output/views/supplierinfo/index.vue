<template>
    <div class="app-container">
      <el-card>
        <y-form
                ref="supplierinfoForm"
                :model="supplierinfoForm"
                label-width="80px"
        >

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

          <el-row type="flex" align="space-between">
            <el-col>
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button @click="reset" class="y-mr-l-10">重置</el-button>
            </el-col>
            <el-button type="success" @click="add">添加供货商及订货</el-button>

          </el-row>
        </y-form>
      </el-card>
        <y-table
            :data="supplierinfosData"
            :pagination="pagination"
            @sortBy="sortBy"
            @changePage4List="getList"
            class="y-p-t-20"
        >
            <template>

                
                    
                        <el-table-column prop="supply_source"
                                         label="货品货源"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="create_at"
                                         label="供应商录入日期"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supplier_code"
                                         label="供货商编码"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="supply_brand"
                                         label="供货品牌"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="authorized_brand"
                                         label="可授权品牌"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="brand_level"
                                         label="品质档次"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="mg_gender"
                                         label="性别"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="mg_series"
                                         label="系列"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="mg_category"
                                         label="品类"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="mg_age"
                                         label="适穿年龄"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="mg_style"
                                         label="基本风格"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="mg_memo"
                                         label="备忘"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="cost_performance"
                                         label="性价比"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="wholesale_mode"
                                         label="起批方式"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="account_period"
                                         label="账期"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="refundable"
                                         label="能否退货"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="good_reliable"
                                         label="商家靠谱度"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                
                    
                        <el-table-column prop="merchant_reliable"
                                         label="货品靠谱度"
                                         align="center"
                                         
                                         
                                          >


                        </el-table-column>
                    
                



                <el-table-column label="操作" width="100px"  align="center">
                    <template slot-scope="{row}">
                        <el-button type="text" size="small" @click="edit(row.id)">修改</el-button>
                      <el-divider direction="vertical"></el-divider>
                      <el-button type="text" size="small" @click="del(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </template>
        </y-table>
    </div>
</template>
<script>
    import {getSupplierinfos, delSupplierinfo} from "@/api/supplierinfo"

    export default {
        data() {
            return {
            supplierinfoForm: {},
            supplierinfosData: [],
                pagination: {
                pageNumber: 1,
                    pageSize: 10
            },
            
        }
        },
        created() {
            this.getList()
        },
        methods: {
            async getList(param) {
                const {data} = await getSupplierinfos(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.supplierinfosData = data.list
                this.pagination.total = data.pagination.total
            },

            add() {
                this.$router.push({path: "add"})
            },
            edit(id) {
                this.$router.push({path: "edit", query: {id}})
            },
            del(id) {
                this.$confirm("是否删除?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning"
                })
                    .then(() => {
                        delSupplierinfo(id).then((response) => {
                            this.$message({
                                type: "success",
                                message: "删除成功!"
                            })
                            this.getList()
                        })
                    })
                    .catch(() => {
                        this.$message({
                            type: "info",
                            message: "已取消删除"
                        })
                    })
            },
            onSearch(sort) {
                this.getList({...this.supplierinfoForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.supplierinfoForm = {}
                this.getList()
            }
        }
    }
</script>

<style lang='scss' scoped>
.app-container {

}
</style>